package com.example.CasadeAposta.service;

import com.example.CasadeAposta.dtos.ApostaDTO;
import com.example.CasadeAposta.dtos.CriarApostaDTO;
import com.example.CasadeAposta.model.Aposta;
import com.example.CasadeAposta.model.Quadrado;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.model.enums.ApostaStatus;
import com.example.CasadeAposta.model.enums.TipoQuadrado;
import com.example.CasadeAposta.repositories.ApostaRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDateTime;
import java.util.*;

@Service
@RequiredArgsConstructor
public class ApostaService {

    private final ApostaRepository apostaRepository;
    private final AuthService authService;

    private final Map<UUID, Quadrado[][]> jogos = new HashMap<>();

    public ApostaDTO criar(CriarApostaDTO data) {

        User userLogado = getUsuarioLogado();

        if (apostaRepository.findByUsuarioAndStatus(userLogado, ApostaStatus.EM_ANDAMENTO).isPresent()) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Não é permitido criar uma aposta com outra em andamento!"
            );
        }

        if (data.valor_apostado() == null) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Valor da aposta é obrigatório"
            );
        }

        Aposta aposta = new Aposta();

        aposta.setUsuario(userLogado);
        aposta.setValorApostado(data.valor_apostado());
        aposta.setValorAtual(data.valor_apostado());
        aposta.setStatus(ApostaStatus.EM_ANDAMENTO);
        aposta.setValorGanhos(BigDecimal.ZERO);
        aposta.setDiamantesEncontrados(0);
        aposta.setBombasEncontradas(0);
        aposta.setPosicoesDiamantes(new ArrayList<>());
        aposta.setDataCriacao(LocalDateTime.now());
        aposta.setDataEncerramento(LocalDateTime.now().plusHours(1));

        aposta = apostaRepository.save(aposta);

        jogos.put(aposta.getId(), gerarCampoMinado());

        return toDTO(aposta);
    }

    private Quadrado[][] gerarCampoMinado() {

        Quadrado[][] matriz = new Quadrado[5][5];

        List<Integer> posicoes = new ArrayList<>();
        for (int i = 0; i < 25; i++) {
            posicoes.add(i);
        }

        Collections.shuffle(posicoes);

        Set<Integer> bombas = new HashSet<>(posicoes.subList(0, 5));

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {

                int pos = i * 5 + j;

                Quadrado quadrado = new Quadrado();
                quadrado.setLinha(i);
                quadrado.setColuna(j);
                quadrado.setRevelado(false);

                if (bombas.contains(pos)) {
                    quadrado.setTipo(TipoQuadrado.BOMBA);
                } else {
                    quadrado.setTipo(TipoQuadrado.DIAMANTE);
                }

                matriz[i][j] = quadrado;
            }
        }

        return matriz;
    }

    public ApostaDTO jogar(int linha, int coluna) {

        ApostaContext contexto = getContextoJogo();
        Aposta aposta = contexto.aposta();
        Quadrado[][] campo = contexto.campo();

        if (linha < 0 || linha >= 5 || coluna < 0 || coluna >= 5) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Posição inválida");
        }

        Quadrado quadrado = campo[linha][coluna];

        if (quadrado.isRevelado()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Quadrado já revelado");
        }

        quadrado.setRevelado(true);

        if (quadrado.getTipo() == TipoQuadrado.BOMBA) {

            List<Integer> bombas = new ArrayList<>();

            for (int i = 0; i < campo.length; i++) {
                for (int j = 0; j < campo[i].length; j++) {
                    if (campo[i][j].getTipo() == TipoQuadrado.BOMBA) {
                        campo[i][j].setRevelado(true);
                        int posicao = i * 5 + j;
                        bombas.add(posicao);
                    }
                }
            }

            aposta.setPosicoesBombas(bombas);
            aposta.setStatus(ApostaStatus.FINALIZADA);
            aposta.setValorAtual(BigDecimal.ZERO);

            apostaRepository.save(aposta);
            jogos.remove(aposta.getId());

            return toDTO(aposta);
        }

        int novosDiamantes = aposta.getDiamantesEncontrados() + 1;
        aposta.setDiamantesEncontrados(novosDiamantes);

        int posicao = linha * 5 + coluna;
        List<Integer> diamantes = aposta.getPosicoesDiamantes();
        if (diamantes == null) {
            diamantes = new ArrayList<>();
        }
        diamantes.add(posicao);
        aposta.setPosicoesDiamantes(diamantes);

        BigDecimal multiplicador = BigDecimal.valueOf(1 + (novosDiamantes * 0.33));

        BigDecimal valorAtual = aposta.getValorApostado()
                .multiply(multiplicador)
                .setScale(2, RoundingMode.HALF_UP);

        aposta.setValorAtual(valorAtual);

        apostaRepository.save(aposta);

        return toDTO(aposta);
    }

    public ApostaDTO encerrar() {

        ApostaContext contexto = getContextoJogo();
        Aposta aposta = contexto.aposta();

        aposta.setValorGanhos(aposta.getValorAtual());
        aposta.setStatus(ApostaStatus.FINALIZADA);

        apostaRepository.save(aposta);
        jogos.remove(aposta.getId());

        return toDTO(aposta);
    }

    private ApostaContext getContextoJogo() {
        User user = getUsuarioLogado();
        Aposta aposta = getApostaEmAndamento(user);
        Quadrado[][] campo = getCampo(aposta.getId());
        return new ApostaContext(aposta, campo);
    }

    private Aposta getApostaEmAndamento(User user) {
        return apostaRepository
                .findByUsuarioAndStatus(user, ApostaStatus.EM_ANDAMENTO)
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND, "Nenhuma aposta em andamento"
                ));
    }

    private Quadrado[][] getCampo(UUID apostaId) {
        Quadrado[][] campo = jogos.get(apostaId);

        if (campo == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Jogo não encontrado");
        }

        return campo;
    }

    private User getUsuarioLogado() {

        String email = SecurityContextHolder
                .getContext()
                .getAuthentication()
                .getName();

        if (email == null) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Usuário não autenticado");
        }

        return authService.buscarPorEmail(email);
    }

    private ApostaDTO toDTO(Aposta aposta) {
        return new ApostaDTO(
                aposta.getValorApostado(),
                aposta.getValorAtual(),
                aposta.getDiamantesEncontrados(),
                aposta.getStatus(),
                aposta.getValorGanhos()
        );
    }

    private record ApostaContext(Aposta aposta, Quadrado[][] campo) {}
}
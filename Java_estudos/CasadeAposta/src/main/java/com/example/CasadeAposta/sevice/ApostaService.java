package com.example.CasadeAposta.sevice;

import com.example.CasadeAposta.dtos.ApostaDTO;
import com.example.CasadeAposta.dtos.CriarApostaDTO;
import com.example.CasadeAposta.dtos.JogarDTO;
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
            throw new RuntimeException("Não é permitido criar uma aposta com outra em andamento!");
        }

        if(data.valor_apostado() == null){
            throw new RuntimeException("Valor da aposta é obrigatório");
        }

        Aposta aposta = new Aposta();

        aposta.setUsuario(userLogado);
        aposta.setValorApostado(data.valor_apostado());
        aposta.setValorAtual(data.valor_apostado());
        aposta.setStatus(ApostaStatus.EM_ANDAMENTO);
        aposta.setValorGanhos(BigDecimal.ZERO);
        aposta.setDiamantesEncontrados(0);
        aposta.setDataCriacao(LocalDateTime.now());
        aposta.setDataEncerramento(LocalDateTime.now().plusHours(1));

        aposta = apostaRepository.save(aposta);

        Quadrado[][] campo = gerarCampoMinado();
        jogos.put(aposta.getId(), campo);

        return new ApostaDTO(
                aposta.getValorApostado(),
                aposta.getValorAtual(),
                aposta.getDiamantesEncontrados(),
                aposta.getStatus()
        );
    }


    private Quadrado[][] gerarCampoMinado(){

        Random random = new Random();
        Quadrado[][] matriz = new Quadrado[5][5];

        for(int i = 0; i < 5; i++){
            for(int j = 0; j < 5; j++){

                Quadrado quadrado = new Quadrado();

                quadrado.setLinha(i);
                quadrado.setColuna(j);
                quadrado.setRevelado(false);
                quadrado.setTipo(TipoQuadrado.DIAMANTE);

                matriz[i][j] = quadrado;
            }
        }

        int bombas = 0;

        while(bombas < 5){

            int linha = random.nextInt(5);
            int coluna = random.nextInt(5);

            if(matriz[linha][coluna].getTipo() != TipoQuadrado.BOMBA){

                matriz[linha][coluna].setTipo(TipoQuadrado.BOMBA);
                bombas++;
            }
        }

        return matriz;
    }


    public ApostaDTO jogar(int linha, int coluna){

        User userLogado = getUsuarioLogado();

        Aposta aposta = apostaRepository
                .findByUsuarioAndStatus(userLogado, ApostaStatus.EM_ANDAMENTO)
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND, "Nenhuma aposta em andamento"
                ));

        UUID apostaId = aposta.getId();
        Quadrado[][] campo = jogos.get(apostaId);

        if(campo == null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND,"Jogo não encontrado");
        }

        if(linha < 0 || linha >= 5 || coluna < 0 || coluna >= 5){
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST,"Posição inválida");
        }

        Quadrado quadrado = campo[linha][coluna];

        if(quadrado.isRevelado()){
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST,"Quadrado já revelado");
        }

        quadrado.setRevelado(true);

        if(quadrado.getTipo() == TipoQuadrado.BOMBA){
            aposta.setStatus(ApostaStatus.FINALIZADA);
            aposta.setValorAtual(BigDecimal.ZERO);
            apostaRepository.save(aposta);
            jogos.remove(apostaId);

            return new ApostaDTO(
                    aposta.getValorApostado(),
                    aposta.getValorAtual(),
                    aposta.getDiamantesEncontrados(),
                    aposta.getStatus()
            );
        }

        if(quadrado.getTipo() == TipoQuadrado.DIAMANTE){

            int novosDiamantes = aposta.getDiamantesEncontrados() + 1;
            aposta.setDiamantesEncontrados(novosDiamantes);

            BigDecimal multiplicador = BigDecimal.valueOf(1 + (novosDiamantes * 0.33));
            BigDecimal valorAtual = aposta.getValorApostado().multiply(multiplicador);

            aposta.setValorAtual(valorAtual);

            apostaRepository.save(aposta);
        }

        return new ApostaDTO(
                aposta.getValorApostado(),
                aposta.getValorAtual(),
                aposta.getDiamantesEncontrados(),
                aposta.getStatus()
        );
    }

    public Aposta encerrar(){

       Aposta aposta = new Aposta();

        UUID apostaId = aposta.getId();

        Quadrado[][] campo = jogos.get(apostaId);

        if(campo == null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND,"Jogo não encontrado");
        }

        long diamantes = 0;

        for(int i = 0; i < 5; i++){
            for(int j = 0; j < 5; j++){

                Quadrado q = campo[i][j];

                if(q.isRevelado() && q.getTipo() == TipoQuadrado.DIAMANTE){
                    diamantes++;
                }
            }
        }

        BigDecimal ganho = aposta.getValorApostado()
                .multiply(BigDecimal.valueOf(1 + (diamantes * 0.33)));

        aposta.setValorGanhos(ganho);
        aposta.setStatus(ApostaStatus.FINALIZADA);

        jogos.remove(apostaId);

        return apostaRepository.save(aposta);
    }


    private User getUsuarioLogado(){

        String email = SecurityContextHolder
                .getContext()
                .getAuthentication()
                .getName();

        if(email == null){
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Usuário não autenticado");
        }

        return authService.buscarPorEmail(email);
    }



}
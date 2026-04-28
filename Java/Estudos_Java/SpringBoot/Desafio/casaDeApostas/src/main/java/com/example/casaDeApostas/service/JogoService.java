package com.example.casaDeApostas.service;

import ch.qos.logback.core.joran.conditional.IfAction;
import com.example.casaDeApostas.dto.CriarJogoDTO;

import com.example.casaDeApostas.model.conta.Account;
import com.example.casaDeApostas.model.enums.TipoJogo;
import com.example.casaDeApostas.model.enums.TipoCampo;
import com.example.casaDeApostas.model.jogo.Jogo;
import com.example.casaDeApostas.model.position.Positions;
import com.example.casaDeApostas.model.users.User;

import com.example.casaDeApostas.repository.AccountRepository;
import com.example.casaDeApostas.repository.JogoRepository;
import com.example.casaDeApostas.repository.PositionsRepository;
import com.example.casaDeApostas.repository.UserRepository;

import jakarta.transaction.Transactional;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.*;


@Service
@AllArgsConstructor
public class JogoService {

    private final UserRepository userRepository;

    private final JogoRepository jogoRepository;

    private final PositionsRepository positionsRepository;

    private final AccountRepository accountRepository;

    public Jogo criarJogo(CriarJogoDTO dto) {

        Optional<User> user = userRepository.findById(dto.userId());

        if (user.isPresent()) {
            Jogo novoJogo = new Jogo(user.get(), dto.valorAposta());

            jogoRepository.save(novoJogo);
            novoJogo.gerarCampoMinado();

            salvarMatriz(novoJogo.getMatriz());
            return novoJogo;
        }

        return new Jogo();
    }


    @Transactional
    public Jogo jogar(UUID idJogo, int linha, int coluna) {

        Optional<Jogo> jogo = jogoRepository.findById(idJogo);

        if (!jogo.isPresent()){
            new Jogo("Jogo não encontrado");
        }

        int indiceReal = (linha * 5) + coluna;

        if (linha < 0 || linha >= 5 || coluna < 0 || coluna >= 5) {
            return new Jogo("Tamanho insuficiente.");
        }
        if (jogo.get().getMatriz()[indiceReal] != TipoCampo.DIAMANTE) {

            if (jogo.get().getPercas() == 1){
                return new Jogo("Você já perdeu.");
            }
            jogo.get().adicionarPerdas(1);
            jogo.get().setTipoDB(TipoCampo.BOMBA);
            jogo.get().setTipoJogo(TipoJogo.ENCERRADO);
            return jogoRepository.save(jogo.get());

        } else {

            jogo.get().adicionarGanhos(1);
            jogo.get().setTipoDB(TipoCampo.DIAMANTE);
            jogo.get().setTipoJogo(TipoJogo.EM_ANDAMENTO);
            jogo.get().adicionarDiamantesEncontrados(1);
            return jogoRepository.save(jogo.get());
        }
    }

    public ResponseEntity<String> encerrarJogo(UUID idJogo) {

        Optional<Jogo> jogo = jogoRepository.findById(idJogo);

        if (jogo.isPresent()) {

            if (jogo.get().getTipoJogo() == TipoJogo.ENCERRADO) {
                return ResponseEntity.status(HttpStatus.CONFLICT).body("jogo já finalizado.");
            }

            jogo.get().setTipoJogo(TipoJogo.ENCERRADO);

            Double ganho = jogo.get().calcularGanho(jogo.get());

            Optional<User> user = userRepository.findById(jogo.get().getUsuario().getId());
            if (user.isPresent()) {

                Account account = accountRepository.findByCpf(user.get().getCpf());
                if (account != null) {
                    account.setValorAtual(ganho);
                    accountRepository.save(account);
                    jogoRepository.save(jogo.get());
                    return ResponseEntity.ok().body("Jogo finalizado.");
                }
                else {
                    return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário encontrado, porque ele não possui uma conta.");
                }
            }
            else {
                return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário não encontrado.");
            }
        }
        else {
            return ResponseEntity.status(HttpStatus.CONFLICT).body("jogo não encontrado.");
        }
    }

    public void salvarMatriz(TipoCampo[] matriz) {

        positionsRepository.deleteAll();

        for (int i = 0; i < matriz.length; i++) {
            Positions posicoes = new Positions(
                    i,
                    matriz[i]
            );
            positionsRepository.save(posicoes);

        }

    }


}
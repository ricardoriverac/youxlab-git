package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.CriarJogoDTO;

import com.example.casaDeApostas.model.enums.TipoJogo;
import com.example.casaDeApostas.model.enums.TipoCampo;
import com.example.casaDeApostas.model.jogo.Jogo;
import com.example.casaDeApostas.model.position.Positions;
import com.example.casaDeApostas.model.users.User;

import com.example.casaDeApostas.repository.JogoRepository;
import com.example.casaDeApostas.repository.PositionsRepository;
import com.example.casaDeApostas.repository.UserRepository;

import jakarta.transaction.Transactional;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.Optional;
import java.util.UUID;


@Service
@AllArgsConstructor
public class JogoService {

    private final UserRepository userRepository;

    private final JogoRepository jogoRepository;

    private final PositionsRepository positionsRepository;

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

        Jogo jogo = jogoRepository.findById(idJogo)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.CONFLICT, "Jogo não encontrado"));

        int indiceReal = (linha * coluna) + coluna;

        if (linha < 0 || linha >= 5 || coluna < 0 || coluna >= 5) {
            throw new ResponseStatusException(HttpStatus.CONFLICT, "Tamanho insuficiente.");
        }
        if (jogo.getMatriz()[indiceReal] != TipoCampo.DIAMANTE) {

            if (jogo.getPercas() == 1){
                throw new ResponseStatusException(HttpStatus.CONFLICT, "Você já perdeu.");
            }
            jogo.adicionarPerdas(1);
            jogo.setTipoDB(TipoCampo.BOMBA);
            jogo.setTipoJogo(TipoJogo.ENCERRADO);
            return jogoRepository.save(jogo);

        } else {

            jogo.adicionarGanhos(1);
            jogo.setTipoDB(TipoCampo.DIAMANTE);
            jogo.setTipoJogo(TipoJogo.EM_ANDAMENTO);
            jogo.adicionarDiamantesEncontrados(1);
            return jogoRepository.save(jogo);
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
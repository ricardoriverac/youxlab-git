package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.CriarJogoDTO;

import com.example.casaDeApostas.dto.EncerrarRespostaDTO;
import com.example.casaDeApostas.dto.JogoResponseDTO;
import com.example.casaDeApostas.exceptions.*;
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
import org.springframework.stereotype.Service;

import java.util.*;


@Service
@AllArgsConstructor
public class JogoService {

    private final UserRepository userRepository;

    private final JogoRepository jogoRepository;

    private final PositionsRepository positionsRepository;

    private final AccountRepository accountRepository;

    public Jogo criarJogo(CriarJogoDTO dto){

        Optional<User> user = userRepository.findById(dto.userId());

        if (user.isPresent()) {
            Jogo novoJogo = new Jogo(user.get(), dto.valorAposta());

            Account account = accountRepository.findByCpf(user.get().getCpf());
            if (account != null) {

                if (account.getValorAtual() < dto.valorAposta()){
                    throw new IllegalArgumentException("Você não possui esse valor na conta.");
                }

                account.tirarValorApostado(dto.valorAposta());
                jogoRepository.save(novoJogo);
                novoJogo.gerarCampoMinado();

                salvarMatriz(novoJogo.getMatriz());
                return novoJogo;
            }
            else {
                throw new YouDoNotHaveBankAccount("Você não possuiu uma conta bancária para jogar.");
            }
        }
        throw new UserDoesNotExist("Erro: Usuário não existe.");
    }


    @Transactional
    public Object jogar(UUID idJogo, int linha, int coluna) {

        Optional<Jogo> jogo = jogoRepository.findById(idJogo);

        if (!jogo.isPresent()){
            throw new JogoNaoEncontrado("Jogo não encontrado");
        }

        if (jogo.get().getTipoJogo() == TipoJogo.ENCERRADO){
            throw new JogoJaEncerrado("Você já perdeu.");
        }

        int indiceReal = (linha * 5) + coluna;

        if (linha < 0 || linha >= 5 || coluna < 0 || coluna >= 5) {
            throw  new IllegalArgumentException("Tamanho insuficiente.");
        }
        if (jogo.get().getMatriz()[indiceReal] != TipoCampo.DIAMANTE) {

            jogo.get().adicionarPerdas(1);
            jogo.get().setTipoDB(TipoCampo.BOMBA);
            jogo.get().setTipoJogo(TipoJogo.ENCERRADO);
            jogo.get().calcularGanho(jogo.get());
            jogoRepository.save(jogo.get());
            return "Voce encontrou uma: "
                    + jogo.get().getTipoDB()
                    + " \n"
                    + "Jogo finalizado.";

        } else {

            jogo.get().adicionarGanhos(1);
            jogo.get().setTipoDB(TipoCampo.DIAMANTE);
            jogo.get().setTipoJogo(TipoJogo.EM_ANDAMENTO);
            jogo.get().adicionarDiamantesEncontrados(1);
            jogo.get().setValorGanho(jogo.get().calcularGanho(jogo.get()));
            jogoRepository.save(jogo.get());
            return new JogoResponseDTO(
                    jogo.get().getTipoDB()
            );
        }
    }

    public EncerrarRespostaDTO encerrarJogo(UUID idJogo) {

        Optional<Jogo> jogo = jogoRepository.findById(idJogo);

        if (jogo.isPresent()) {

            if (jogo.get().getTipoJogo() == TipoJogo.ENCERRADO) {
                throw new JogoJaEncerrado("Jogo já encerrado.");
            }

            jogo.get().setTipoJogo(TipoJogo.ENCERRADO);

            Double ganho = jogo.get().calcularGanho(jogo.get());

            Optional<User> user = userRepository.findById(jogo.get().getUsuario().getId());
            if (user.isPresent()) {

                Account account = accountRepository.findByCpf(user.get().getCpf());
                if (account != null) {

                    account.depositar(ganho);
                    EncerrarRespostaDTO encerrarRespostaDTO = new EncerrarRespostaDTO("Jogo Finalizado.", jogo.get().getValorGanho());
                    accountRepository.save(account);
                    jogoRepository.save(jogo.get());
                    return encerrarRespostaDTO;

                } else {
                    throw new UserExistButNotAccount("Usuário encontrado, mas ele não possui uma conta.");
                }
            } else {
                throw new UserDoesNotExist("Usuário não encontrado.");
            }
        } else {
            throw new JogoNaoEncontrado("jogo não encontrado.");
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
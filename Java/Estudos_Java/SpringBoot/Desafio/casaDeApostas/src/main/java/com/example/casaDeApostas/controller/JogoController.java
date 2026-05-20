package com.example.casaDeApostas.controller;

import com.example.casaDeApostas.dto.*;

import com.example.casaDeApostas.exceptions.*;
import com.example.casaDeApostas.model.enums.TipoJogo;
import com.example.casaDeApostas.model.jogo.Jogo;
import com.example.casaDeApostas.repository.JogoRepository;
import com.example.casaDeApostas.service.JogoService;

import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import java.util.UUID;


@RestController
@RequestMapping("/jogos")
@AllArgsConstructor
public class JogoController {

    private final JogoService jogoService;

    private final JogoRepository jogoRepository;

    @PostMapping("/criar-jogo")
    public ResponseEntity criarJogo(@RequestBody CriarJogoDTO criarJogoDTO){

        try {
            if (criarJogoDTO.valorAposta() <= 0.0) {
                return ResponseEntity.status(HttpStatus.CONFLICT).body("Valor não permitido para apostar.");
            }

            Jogo jogar = jogoService.criarJogo(criarJogoDTO);
            return ResponseEntity.ok().body(jogar);
        }
        catch (YouDoNotHaveBankAccount e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Você não possuiu uma conta bancária para jogar.");
        }
        catch (IllegalArgumentException e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Saldo insuficiente.");
        }
        catch (UserDoesNotExist e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Erro: Usuário não existe.");
        }
    }

    @PostMapping("/jogar")
    public ResponseEntity jogar(
            @RequestBody ApostaDTO dto) {

        try {

            Object jogoDados = jogoService.jogar(dto.idJogo(), dto.linha(), dto.coluna());
            return ResponseEntity.status(HttpStatus.OK).body(jogoDados);

        }
        catch (JogoJaEncerrado e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Você já perdeu.");
        }
        catch (IllegalArgumentException e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Tamanho insuficiente.");
        }
        catch (JogoNaoEncontrado e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Jogo não existe.");
        }
        catch (UserExistButNotAccount e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário existe, mas ele não possui uma conta bancária no jogo.");
        }

    }

    @PutMapping("/encerrar")
    public ResponseEntity encerrarJogo(@RequestBody EncerrarDTO dto){

        try {
            EncerrarRespostaDTO resposta = jogoService.encerrarJogo(dto.idJogo());
            return ResponseEntity.status(HttpStatus.OK).body(resposta);

        }
        catch (JogoNaoEncontrado e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Jogo não existe.");
        }
        catch (JogoJaEncerrado e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Jogo já encerrado.");
        }
        catch (UserDoesNotExist e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário não existe.");
        }
        catch (UserExistButNotAccount e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário existe, mas ele não possui uma conta.");
        }
    }

}

package com.example.casaDeApostas.controller;

import com.example.casaDeApostas.dto.ApostaDTO;
import com.example.casaDeApostas.dto.CriarJogoDTO;

import com.example.casaDeApostas.dto.JogoResponseDTO;
import com.example.casaDeApostas.model.enums.TipoJogo;
import com.example.casaDeApostas.model.jogo.Jogo;
import com.example.casaDeApostas.repository.JogoRepository;
import com.example.casaDeApostas.service.JogoService;

import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;


@RestController
@RequestMapping("/jogos")
@AllArgsConstructor
public class JogoController {

    private final JogoService jogoService;

    private final JogoRepository jogoRepository;

    @PostMapping("/criar-jogo")
    public ResponseEntity criarJogo(@RequestBody CriarJogoDTO criarJogoDTO){

        if (criarJogoDTO.valorAposta() <= 0.0){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Valor não permitido para apostar.");
        }

        Jogo jogar = jogoService.criarJogo(criarJogoDTO);
        return ResponseEntity.ok().body(jogar);
    }

    @PostMapping("/jogar")
    public ResponseEntity jogar(
            @RequestBody ApostaDTO dto) {

        Optional<Jogo> procurarJogo = jogoRepository.findById(dto.idJogo());

        if (procurarJogo.isPresent()) {
            Jogo jogoAtualizado = procurarJogo.get();
            jogoAtualizado = jogoService.jogar(dto.idJogo(), dto.linha(), dto.coluna());

            if (jogoAtualizado.getTipoJogo() == TipoJogo.ENCERRADO) {

                return ResponseEntity.status(HttpStatus.CONFLICT).body(
                        "Voce encontrou uma: "
                                + jogoAtualizado.getTipoDB()
                                + " \n"
                                + "Jogo finalizado.");
            }

            JogoResponseDTO dadosJogo = new JogoResponseDTO(
                    jogoAtualizado.getValorApostado(),
                    jogoAtualizado.getTipoDB()
            );
            return ResponseEntity.status(HttpStatus.OK).body(dadosJogo);
        }

        return ResponseEntity.status(HttpStatus.CONFLICT).body("Jogo não existe.");
    }
//
//    @PostMapping("/encerrar")
//    public ResponseEntity encerrar(@RequestBody EncerrarDTO dto) {
//
//        Jogo jogo = new Jogo();
//
//        return ResponseEntity.ok().body(jogo.encerrar(dto));
//    }

}

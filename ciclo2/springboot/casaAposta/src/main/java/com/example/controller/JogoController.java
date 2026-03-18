package com.example.controller;



import com.example.dto.JogadaResponseDTO;
import com.example.dto.JogoRequestDTO;
import com.example.dto.JogoResponseDTO;
import com.example.model.Jogo;
import com.example.model.User;
import com.example.service.JogoService;
import com.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

import static com.example.enuns.StatusJogo.*;


@RestController
@RequestMapping("/jogo")

public class JogoController {

        @Autowired
        private JogoService jogoService;

        @Autowired
        private UserService userService;

        @PostMapping("/iniciar")
        public ResponseEntity iniciarJogo(@RequestBody JogoRequestDTO dados) {
            try {
                User user = userService.buscarPorId(dados.userId());

                if (dados.valorAposta().doubleValue() < 1.0) {
                    return ResponseEntity.badRequest().body("Valor mínimo da aposta é R$ 1,00");
                }

                Jogo jogo = jogoService.iniciarJogo(user, dados.valorAposta());

                JogoResponseDTO response = new JogoResponseDTO(
                        jogo.getId(),
                        jogo.getValorAposta(),
                        jogo.getValorAcumulado(),
                        jogo.getStatus(),
                        jogo.getDiamantesEncontrados(),
                        jogo.getTabuleiroVisivel()
                );

                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao iniciar jogo: " + e.getMessage());
            }
        }

        @PostMapping("/jogar")
        public ResponseEntity fazerJogada(@RequestBody Map<String, Object> dados) {
            try {
                Long jogoId = Long.parseLong(dados.get("jogoId").toString());
                int linha = Integer.parseInt(dados.get("linha").toString());
                int coluna = Integer.parseInt(dados.get("coluna").toString());

                Map<String, Object> resultado = jogoService.processarJogada(jogoId, linha, coluna);

                Jogo jogo = jogoService.buscarJogoPorId(jogoId);

                Map<String, Object> response = new HashMap<>();
                response.put("tipoCelula", resultado.get("tipoCelula"));
                response.put("valorAcumulado", resultado.get("novoValorAcumulado"));
                response.put("status", resultado.get("statusJogo"));
                response.put("mensagem", resultado.get("mensagem"));

                response.put("jogoFinalizado", jogo.getStatus() != EM_ANDAMENTO);
                response.put("venceu", jogo.getStatus() == GANHOU);
                response.put("diamantesEncontrados", jogo.getDiamantesEncontrados());

                return ResponseEntity.ok(response);

            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao processar jogada: " + e.getMessage());
            }
        }


        @PostMapping("/encerrar/{jogoId}")
        public ResponseEntity encerrarJogo(@PathVariable Long jogoId) {
            try {
                Map<String, Object> resultado = jogoService.encerrarJogo(jogoId);
                BigDecimal valorGanho = (BigDecimal) resultado.get("valorGanho");
                return ResponseEntity.ok(new JogadaResponseDTO(
                        null,
                        valorGanho,
                        ENCERRADO,
                        true,
                        "Jogo encerrado! Você ganhou R$ " + valorGanho
                ));
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao encerrar jogo: " + e.getMessage());
            }
        }

        @GetMapping("/atual/{userId}")
        public ResponseEntity jogoAtual(@PathVariable Long userId) {
            try {
                var jogo = jogoService.buscarJogoAtual(userId);
                if (jogo == null) {
                    return ResponseEntity.ok("Nenhum jogo em andamento");
                }

                JogoResponseDTO response = new JogoResponseDTO(
                        jogo.getId(),
                        jogo.getValorAposta(),
                        jogo.getValorAcumulado(),
                        jogo.getStatus(),
                        jogo.getDiamantesEncontrados(),
                        jogo.getTabuleiroVisivel()
                );

                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao buscar jogo atual: " + e.getMessage());
            }
        }
    }





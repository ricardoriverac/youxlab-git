package com.example.service;


import com.example.enuns.StatusJogo;
import com.example.enuns.TipoCelula;
import com.example.model.Jogada;
import com.example.model.Jogo;
import com.example.model.User;
import com.example.repository.JogadaRepository;
import com.example.repository.JogoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@Service
public class JogoService {

    @Autowired
    private JogoRepository jogoRepository;

    @Autowired
    private JogadaRepository jogadaRepository;


    public Jogo iniciarJogo(User user, BigDecimal valorAposta) {
        Optional<Jogo> jogoExistente = jogoRepository.findByUserIdAndStatus(user.getId(), StatusJogo.EM_ANDAMENTO);
        if (jogoExistente.isPresent()) {
            throw new RuntimeException("Você já tem um jogo em andamento. Termine ele antes de começar outro.");
        }

        Jogo jogo = new Jogo(user, valorAposta);
        return jogoRepository.save(jogo);
    }


    public Map<String, Object> processarJogada(Long jogoId, int linha, int coluna) {

        if (linha < 0 || linha > 4 || coluna < 0 || coluna > 4) {
            throw new RuntimeException("Posição inválida! Linha e coluna devem ser de 0 a 4.");
        }

        Jogo jogo = jogoRepository.findById(jogoId)
                .orElseThrow(() -> new RuntimeException("Jogo não encontrado"));


        if (jogo.getStatus() != StatusJogo.EM_ANDAMENTO) {
            throw new RuntimeException("Este jogo já foi finalizado. Status: " + jogo.getStatus());
        }

        boolean jaJogou = jogadaRepository.existsByJogoIdAndPosicao(jogoId, linha, coluna);
        if (jaJogou) {
            throw new RuntimeException("Você já clicou nessa posição!");
        }

        BigDecimal valorAntes = jogo.getValorAcumulado();
        int diamantesAntes = jogo.getDiamantesEncontrados();

        TipoCelula resultado = jogo.processarJogada(linha, coluna);

        Jogada jogada = new Jogada(
                jogo,
                jogo.getUser(),
                linha,
                coluna,
                resultado,
                valorAntes,
                jogo.getValorAcumulado(),
                jogo.getDiamantesEncontrados(),
                jogo.getJogadasRealizadas()
        );

        jogadaRepository.save(jogada);
        jogoRepository.save(jogo);

        Map<String, Object> resultadoMap = new HashMap<>();
        resultadoMap.put("tipoCelula", resultado.name());
        resultadoMap.put("novoValorAcumulado", jogo.getValorAcumulado());
        resultadoMap.put("statusJogo", jogo.getStatus().name());
        resultadoMap.put("jogoFinalizado", jogo.getStatus() != StatusJogo.EM_ANDAMENTO);
        resultadoMap.put("diamantesEncontrados", jogo.getDiamantesEncontrados());

        String mensagem = gerarMensagemResultado(resultado, jogo.getValorAcumulado());
        resultadoMap.put("mensagem", mensagem);

        return resultadoMap;
    }


    public Map<String, Object> encerrarJogo(Long jogoId) {
        Jogo jogo = jogoRepository.findById(jogoId)
                .orElseThrow(() -> new RuntimeException("Jogo não encontrado"));

        if (jogo.getStatus() != StatusJogo.EM_ANDAMENTO) {
            throw new RuntimeException("Este jogo não está em andamento");
        }

        jogo.encerrar();
        jogoRepository.save(jogo);

        Map<String, Object> resultado = new HashMap<>();
        resultado.put("valorGanho", jogo.getValorGanho());
        resultado.put("diamantesEncontrados", jogo.getDiamantesEncontrados());
        resultado.put("mensagem", "Jogo encerrado! Você ganhou R$ " + jogo.getValorGanho());

        return resultado;
    }


    public Jogo buscarJogoPorId(Long jogoId) {
        return jogoRepository.findById(jogoId)
                .orElseThrow(() -> new RuntimeException("Jogo não encontrado"));
    }


    public Jogo buscarJogoAtual(Long userId) {
        return jogoRepository.findByUserIdAndStatus(userId, StatusJogo.EM_ANDAMENTO)
                .orElse(null);
    }


    public Map<String, Object> getEstatisticasUser(Long userId) {
        Map<String, Object> stats = new HashMap<>();

        stats.put("totalJogos", jogoRepository.countByUserId(userId));
        stats.put("totalGanho", jogoRepository.somarValorGanhoPorUser(userId));
        stats.put("maiorGanho", jogoRepository.encontrarMaiorGanhoPorUser(userId));
        stats.put("totalDiamantes", jogadaRepository.countDiamantesByUserId(userId));
        stats.put("totalBombas", jogadaRepository.countByUserIdAndTipoCelula(userId, TipoCelula.BOMBA));

        return stats;
    }

    public void validarValorAposta(BigDecimal valorAposta) {
        if (valorAposta == null || valorAposta.doubleValue() < 1.0) {
            throw new RuntimeException("Valor da aposta deve ser no mínimo R$ 1,00");
        }
    }

    private String gerarMensagemResultado(TipoCelula tipo, BigDecimal valorAtual) {
        switch (tipo) {
            case DIAMANTE:
                return " Você encontrou um diamante! Prêmio atual: R$ " + valorAtual;
            case DIAMANTE_VITORIA:
                return " PARABÉNS! Você encontrou todos os 10 diamantes! Prêmio final: R$ " + valorAtual;
            case BOMBA:
                return " BOOM! Você encontrou uma bomba e perdeu tudo!";
            case JA_REVELADO:
                return "Essa posição já foi revelada!";
            default:
                return "";
        }
    }


    public BigDecimal calcularMultiplicador(int diamantesEncontrados) {
        double multiplicador = 1 + (diamantesEncontrados * 0.33);
        return BigDecimal.valueOf(multiplicador);
    }

    public BigDecimal calcularValorAcumulado(BigDecimal valorAposta, int diamantesEncontrados) {
        BigDecimal multiplicador = calcularMultiplicador(diamantesEncontrados);
        return valorAposta.multiply(multiplicador);
    }

}









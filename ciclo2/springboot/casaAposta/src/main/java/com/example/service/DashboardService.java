package com.example.service;

import com.example.dto.DashboardAdminDTO;
import com.example.dto.DashboardUserDTO;
import com.example.enuns.TipoCelula;
import com.example.model.Jogo;
import com.example.repository.JogadaRepository;
import com.example.repository.JogoRepository;
import com.example.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class DashboardService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private JogoRepository jogoRepository;

    @Autowired
    private JogadaRepository jogadaRepository;

    @Autowired
    private UserService userService;


    public DashboardAdminDTO obterDadosAdmin() {
        DashboardAdminDTO dashboard = new DashboardAdminDTO();

        dashboard.setValorTotalGanho(jogoRepository.somarValorGanhoTotal());
        if (dashboard.getValorTotalGanho() == null) {
            dashboard.setValorTotalGanho(BigDecimal.ZERO);
        }

        dashboard.setTotalUser(userRepository.count());


        BigDecimal maiorGanho = jogoRepository.encontrarMaiorGanhoTotal();
        dashboard.setMaiorGanho(maiorGanho != null ? maiorGanho : BigDecimal.ZERO);

        List<Map<String, Object>> ultimosJogos = new ArrayList<>();
        List<Jogo> jogosRecentes = jogoRepository.findTop10ByOrderByDataInicioDesc();

        for (Jogo jogo : jogosRecentes) {
            Map<String, Object> jogoMap = new HashMap<>();
            jogoMap.put("id", jogo.getId());
            jogoMap.put("user", jogo.getUser().getNome());
            jogoMap.put("valorAposta", jogo.getValorAposta());
            jogoMap.put("valorGanho", jogo.getValorGanho());
            jogoMap.put("status", jogo.getStatus().toString());
            jogoMap.put("data", jogo.getDataInicio().format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm")));
            ultimosJogos.add(jogoMap);
        }
         return dashboard;
    }

    public DashboardUserDTO obterDadosUser (Long userId){
        DashboardUserDTO dashboard = new DashboardUserDTO();


        BigDecimal totalGanho = jogoRepository.somarValorGanhoPorUser(userId);
        dashboard.setTotalGanho(totalGanho != null ? totalGanho : BigDecimal.ZERO);


        Double mediaAposta = jogoRepository.calcularMediaApostaPorUser(userId);
        dashboard.setMediaAposta(mediaAposta != null ?
                BigDecimal.valueOf(mediaAposta).setScale(2, RoundingMode.HALF_UP) :
                BigDecimal.ZERO);

        Long totalDiamantes = jogadaRepository.countDiamantesByUserId(userId);
        dashboard.setTotalDiamantesEncontrados(totalDiamantes != null ? totalDiamantes : 0L);

        Long totalBombas = jogadaRepository.countByUserIdAndTipoCelula(userId, TipoCelula.BOMBA);
        dashboard.setTotalBombasEncontradas(totalBombas != null ? totalBombas : 0L);

        return dashboard;
    }


}




package com.example.casaDeApostas.service;

import com.example.casaDeApostas.model.dashboard.DashBoardUser;
import com.example.casaDeApostas.model.dashboard.DashBoardAdmin;

import com.example.casaDeApostas.model.enums.Roles;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.JogoRepository;
import com.example.casaDeApostas.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.*;


@Service
@AllArgsConstructor
public class DashBoardsService {

    private final JogoRepository jogoRepository;

    public DashBoardAdmin dashBoardsAdmin(){

        Long qtdJogos = jogoRepository.countAll();
        Double valorTotal = jogoRepository.ValorCadaPartida();
        return new DashBoardAdmin(qtdJogos, valorTotal);
    }

    public DashBoardUser dashBoardsUser(UUID idUser){

        Long qtdJogos = jogoRepository.countJogoByUsuario_Id(idUser);
        Integer percas = jogoRepository.contarPercasPorUsuario(idUser);
        Integer ganhos = jogoRepository.contarGanhosPorUsuario(idUser);

        DashBoardUser dashBoardUser = new DashBoardUser(qtdJogos, ganhos, percas);
        return dashBoardUser;

    }

}

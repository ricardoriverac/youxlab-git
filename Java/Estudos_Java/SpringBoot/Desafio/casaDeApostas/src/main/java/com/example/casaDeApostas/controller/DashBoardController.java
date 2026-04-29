package com.example.casaDeApostas.controller;

import com.example.casaDeApostas.exceptions.JogoNaoEncontrado;
import com.example.casaDeApostas.model.dashboard.DashBoardAdmin;
import com.example.casaDeApostas.model.dashboard.DashBoardUser;
import com.example.casaDeApostas.repository.UserRepository;
import com.example.casaDeApostas.service.DashBoardsService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

import java.util.UUID;

@RestController
@RequestMapping("/dashboard")
@AllArgsConstructor
public class DashBoardController {

    private DashBoardsService dashBoardsService;

    @GetMapping("/dashboard-admin")
    public ResponseEntity dashboardAdmin(){

        try {
            DashBoardAdmin dashBoardAdmin = dashBoardsService.dashBoardsAdmin();
            return ResponseEntity.ok().body(dashBoardAdmin);
        }
        catch (Exception e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Ocorreu um problema nessa operação.");
        }
    }

    @GetMapping("/dashboard-user/{idUser}")
    public ResponseEntity dashboardUser(@PathVariable UUID idUser){
        try{
            DashBoardUser dashBoardUser = dashBoardsService.dashBoardsUser(idUser);
            return ResponseEntity.ok().body(dashBoardUser);
        }
        catch (Exception e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário não existe.");
        }
    }
}

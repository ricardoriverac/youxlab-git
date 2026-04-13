package com.example.casaDeApostas.controller;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTCreator;
import com.example.casaDeApostas.dto.LoginDTO;
import com.example.casaDeApostas.model.enums.Roles;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.service.*;
import jakarta.validation.Valid;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/casa-apostas")
@AllArgsConstructor
public class ApostaController {

    private final EsquecerSenhaService senhaService;

    private final ApostaService apostaService;

    @PutMapping("/reset-password")
    public ResponseEntity resetarSenha(@RequestBody @Valid User user){

        senhaService.resetarSenha(user);

        return ResponseEntity.ok().body("Senha nova registrada.");
    }

    @PostMapping("/login")
    public ResponseEntity login(@RequestBody @Valid LoginDTO login){

        String token = apostaService.login(login);

        return ResponseEntity.ok().body(token);

    }

}

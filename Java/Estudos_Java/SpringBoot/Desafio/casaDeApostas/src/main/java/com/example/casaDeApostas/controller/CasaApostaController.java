package com.example.casaDeApostas.controller;

import com.example.casaDeApostas.dto.LoginDTO;
import com.example.casaDeApostas.dto.ResetPasswordDTO;
import com.example.casaDeApostas.exceptions.EmailSenhaIncorretos;
import com.example.casaDeApostas.exceptions.UserDoesNotExist;
import com.example.casaDeApostas.exceptions.UsuaroBloqueado;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.UserRepository;
import com.example.casaDeApostas.service.*;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/casa-apostas")
@AllArgsConstructor
public class CasaApostaController {

    private EsquecerSenhaService senhaService;

    private ApostaService apostaService;

    @PostMapping("/reset-password")
    public ResponseEntity resetPassword(@RequestBody ResetPasswordDTO resetar){

        try {
            String resposta = senhaService.resetarSenha(resetar.idUsuario(), resetar.senha());
            return ResponseEntity.status(HttpStatus.OK).body(resposta);
        }
        catch (UserDoesNotExist e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário não existe.");
        }
    }

    @PostMapping("/login")
    public ResponseEntity login(@RequestBody LoginDTO login){

        try {
            String token = apostaService.login(login);
            return ResponseEntity.ok().body(token);
        }
        catch (EmailSenhaIncorretos e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Email ou senha incorretos.");
        }
        catch (UsuaroBloqueado e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário está bloqueado.");
        }

    }

}

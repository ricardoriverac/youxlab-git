package com.example.CasadeAposta.controller;

import com.example.CasadeAposta.dtos.AuthDTO;

import com.example.CasadeAposta.service.AuthService;
import com.example.CasadeAposta.service.PasswordResetService;
import lombok.RequiredArgsConstructor;

import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/auth")
@RequiredArgsConstructor
public class AuthController {

    private final AuthService authService;
    private final PasswordResetService passwordResetService;

    @PostMapping("/login")
    public Map<String,String> login(@RequestBody AuthDTO dto){

        String token = authService.login(dto.email(), dto.senha());

        return Map.of("token", token);
    }

    @PostMapping("/reset-password")
    public String solicitarReset(@RequestParam String email){

        passwordResetService.solicitarReset(email);

        return "Email de reset enviado";
    }

    @PostMapping("/reset-password/confirm")
    public String resetarSenha(@RequestParam String token,
                               @RequestParam String novaSenha){

        passwordResetService.resetarSenha(token,novaSenha);

        return "Senha alterada";
    }
}
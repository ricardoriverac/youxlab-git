package com.example.desafioJoao.controllers;

import com.example.desafioJoao.dtos.LoginDTO;
import com.example.desafioJoao.dtos.LoginResponseDTO;
import com.example.desafioJoao.services.AuthenticationService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class authController {

    private final AuthenticationService service;

    public authController(AuthenticationService service) {
        this.service = service;
    }

    @PostMapping("/login")
    public ResponseEntity login(@RequestBody @Valid LoginDTO data){
    String token = service.loginUser(data);
        return ResponseEntity.ok(new LoginResponseDTO(token));
    }



}

package com.example.CasadeAposta.controller;

import com.example.CasadeAposta.dtos.ApostaDTO;
import com.example.CasadeAposta.dtos.CriarApostaDTO;
import com.example.CasadeAposta.dtos.JogarDTO;
import com.example.CasadeAposta.model.Aposta;
import com.example.CasadeAposta.model.Quadrado;
import com.example.CasadeAposta.sevice.ApostaService;

import lombok.RequiredArgsConstructor;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/apostas")
@RequiredArgsConstructor
public class ApostaController {

    private final ApostaService apostaService;

    @PostMapping
    @PreAuthorize("hasAnyRole('USER','ADMIN')")
    public ApostaDTO criar(@RequestBody CriarApostaDTO dto) {

        return apostaService.criar(dto);
    }


    @PreAuthorize("hasAnyRole('USER', 'ADMIN')")
    @PostMapping("/jogar")
    public ApostaDTO jogar(@RequestBody JogarDTO dto) {
        return apostaService.jogar(dto.linha(), dto.coluna());
    }


    @PostMapping("/encerrar")
    public Aposta encerrar() {
        return apostaService.encerrar();
    }
}
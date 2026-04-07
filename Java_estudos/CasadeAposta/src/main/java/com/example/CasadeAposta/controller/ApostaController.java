package com.example.CasadeAposta.controller;


import com.example.CasadeAposta.dtos.ApostaDTO;
import com.example.CasadeAposta.dtos.CriarApostaDTO;
import com.example.CasadeAposta.dtos.JogarDTO;
import com.example.CasadeAposta.service.ApostaService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

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
    public ApostaDTO encerrar() {
        return apostaService.encerrar();
    }
}
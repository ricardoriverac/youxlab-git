package com.example.CasadeAposta.dtos;

import com.fasterxml.jackson.annotation.JsonIgnore;

import java.util.UUID;

public record JogarDTO(
        int linha,
        int coluna
) {}
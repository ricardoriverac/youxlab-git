package com.example.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

public record LoginResponseDTO(

        @JsonProperty("token")
                String token,

        @JsonProperty("userId")
        Long userId,

        @JsonProperty("nome")
        String nome,

        @JsonProperty("email")
        String email,

        @JsonProperty("role")
        String role,

        @JsonProperty("status")
        String status,

        @JsonProperty("emailConfirmado")
        Boolean emailConfirmado

) {
    public LoginResponseDTO(String token, Long userId, String nome, String role) {
        this(token, userId, nome, null, role, null, null);
    }

    public LoginResponseDTO(String token, Long userId, String nome, String email,
                            String role, String status, Boolean emailConfirmado) {
        this.token = token;
        this.userId = userId;
        this.nome = nome;
        this.email = email;
        this.role = role;
        this.status = status;
        this.emailConfirmado = emailConfirmado;
    }

}

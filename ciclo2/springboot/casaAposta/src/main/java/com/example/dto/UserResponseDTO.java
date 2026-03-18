package com.example.dto;

import com.example.enuns.PerfilUser;
import com.example.enuns.StatusUser;
import com.fasterxml.jackson.annotation.JsonFormat;

import java.time.LocalDate;
import java.time.LocalDateTime;

public record UserResponseDTO(

        Long id,

        String nome,

        String email,

        @JsonFormat(pattern = "dd/MM/yyyy")
        LocalDate dataNascimento,

        PerfilUser role,

        StatusUser status,

        Boolean emailConfirmado,

        @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
        LocalDateTime dataCadastro,

        @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
        LocalDateTime ultimoLogin

) {
    public UserResponseDTO(Long id, String nome, String email, LocalDate dataNascimento,
                              PerfilUser role, StatusUser status, Boolean emailConfirmado) {
        this(id, nome, email, dataNascimento, role, status, emailConfirmado, null, null);
    }

}


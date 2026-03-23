package com.example.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.Size;

import java.time.LocalDate;

public record UserUpdateDTO(

        @Size(min = 3, max = 100, message = "Nome deve ter entre 3 e 100 caracteres")
        String nome,

        @Email(message = "Email inválido")
        String email,

        @JsonFormat(pattern = "dd/MM/yyyy")
        LocalDate dataNascimento

) {

}


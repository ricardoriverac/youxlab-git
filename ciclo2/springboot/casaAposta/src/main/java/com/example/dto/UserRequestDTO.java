package com.example.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.*;

import java.time.LocalDate;

public record UserRequestDTO(

        @NotBlank(message = "Nome é obrigatório")
        @Size(min = 3, max = 100, message = "Nome deve ter entre 3 e 100 caracteres")
                String nome,

        @NotBlank(message = "Email é obrigatório")
        @Email(message = "Email inválido")
        String email,

        @NotNull(message = "Data de nascimento é obrigatória")
        @Past(message = "Data de nascimento deve ser no passado")
        @JsonFormat(pattern = "yyyy/MM/dd")
        LocalDate dataNascimento,

        @NotBlank(message = "Senha é obrigatória")
        @Size(min = 8, message = "Senha deve ter no mínimo 8 caracteres, sendo ela uma letra maiúscula e um número obrigatórios!")
        @Pattern(
                regexp = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>\\/?]).{8,}$",
                message = "Senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial"
        )
        String senha,

        @NotBlank(message = " Aconfirmação de senha é obrigatória")
        @JsonProperty("confirmacaoSenha")
        String confirmacaoSenha

) {


    public boolean senhasConferem() {
        return senha != null && senha.equals(confirmacaoSenha);
    }

}

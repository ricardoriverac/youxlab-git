package com.walter.pedidosapi.dtos;


import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;
import org.hibernate.validator.constraints.ScriptAssert;

@Schema(name = "User")
public record RegisterDTO(
        @NotBlank(message = "é obrigatório o usuário ter um nome")
        @Schema(name = "nome")
        @JsonProperty("nome")
        String name,
        @Email(message = "é obrigatório o e-mail ter o formato correto")
        @NotBlank(message = "é obrigatório o usuário ter um email")
        @Schema(name = "email")
        @JsonProperty("email")
        String email,
        @NotBlank(message = "é obrigatório o usuário ter uma senha")
        @Pattern(regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&]).{8,}$", message = "A senha deve ter no mínimo 8 caracteres, uma letra maíuscula, uma letra minúscula e um número e um caractere especial")
        @Size(min = 8)
        @Schema(name = "senha")
        @JsonProperty("senha")
        String password
        )
{}

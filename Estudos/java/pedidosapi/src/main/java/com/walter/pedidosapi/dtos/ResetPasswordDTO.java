package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

@Schema(name = "ResetPassword")
public record ResetPasswordDTO(
        @Schema(name = "token") @JsonProperty("token")String token,

        @NotBlank(message = "é obrigatório o usuário ter uma senha")
        @Pattern(regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&]).{8,}$", message = "A senha deve ter no mínimo 8 caracteres, uma letra maíuscula, uma letra minúscula e um número e um caractere especial")
        @Size(min = 8)
        @Schema(name = "novaSenha") @JsonProperty("novaSenha")String newPassword){
}
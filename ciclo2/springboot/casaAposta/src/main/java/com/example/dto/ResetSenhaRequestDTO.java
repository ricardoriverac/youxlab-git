package com.example.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

public record ResetSenhaRequestDTO(

    @Email(message = "Email inválido")
    @NotBlank(message = "Email é obrigatório")
    String email,

    String token,

    @Size(min = 8, message = "Senha deve ter no mínimo 8 caracteres")
    @Pattern(
            regexp = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>\\/?]).{8,}$",
            message = "Senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial"
    )
    String novaSenha,

    String confirmacaoSenha

) {

    public boolean senhasConferem() {
        if (novaSenha == null || confirmacaoSenha == null) {
            return false;
        }
        return novaSenha.equals(confirmacaoSenha);
    }
    public boolean isReset() {
        return token != null && !token.isEmpty() &&
                novaSenha != null && !novaSenha.isEmpty() &&
                confirmacaoSenha != null && !confirmacaoSenha.isEmpty();
    }

}


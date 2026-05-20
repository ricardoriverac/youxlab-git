package com.example.casaDeApostas.dto;
import java.util.UUID;

public record ResetPasswordDTO(UUID idUsuario, String senha) {
}

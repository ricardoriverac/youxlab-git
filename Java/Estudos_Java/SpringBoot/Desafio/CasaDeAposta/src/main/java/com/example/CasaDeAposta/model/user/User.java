package com.example.CasaDeAposta.model.user;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;
import lombok.Data;
import lombok.RequiredArgsConstructor;

import java.time.LocalDate;
import java.util.UUID;

@Entity
@Table(name = "users")
@Data
@RequiredArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private String id;

    @NotBlank(message = "Campo obrigatório")
    private String name;

    @NotBlank(message = "Campo obrigatório")
    private String email;

    @NotBlank(message = "Campo obrigatório")
    private LocalDate dataNascimento;

    @NotBlank(message = "Senha Obrigatória")
    @Size(min = 8)
    @Pattern(regexp = "^(?=.*[A-Z])(?=.*\\d).+$")
    private String senha;

    @NotBlank(message = "Senha Diferente")
    private String confirmacaoSenha;
}

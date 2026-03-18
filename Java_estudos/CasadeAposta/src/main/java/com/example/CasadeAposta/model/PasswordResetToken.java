package com.example.CasadeAposta.model;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class PasswordResetToken {

    @Id
    @GeneratedValue
    private Long id;

    private String token;

    private LocalDateTime dataExpiracao;

    private boolean usado = false;

    @ManyToOne
    private User usuario;
}

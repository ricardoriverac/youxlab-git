package com.example.casaDeApostas.model.conta;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Reference;

import java.util.UUID;

@Entity
@Table(name = "contas")
@Data
@NoArgsConstructor
public class Account {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @NotNull
    private Long cpf;

    @NotNull
    private Double valorAtual;


    public Account(Long cpf, Double valorAtual) {
        this.cpf = cpf;
        this.valorAtual = valorAtual;
    }
}

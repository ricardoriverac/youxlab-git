package com.example.casaDeApostas.model.conta;

import com.example.casaDeApostas.dto.DepositoDTO;
import com.example.casaDeApostas.model.jogo.Jogo;
import com.example.casaDeApostas.repository.AccountRepository;
import com.example.casaDeApostas.service.JogoService;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.UUID;

@Entity
@Table(name = "contas")
@Data
public class Account {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @NotNull
    private Long cpf;

    @NotNull
    private Double valorAtual;

    public Account() {}

    public Account(Long cpf, Double valorAtual) {
        this.cpf = cpf;
        this.valorAtual = valorAtual;
    }


    public void depositar(Double valor) {
        if (valor <= 0) {
            throw new IllegalArgumentException("Valor não permitido.");
        }
        else {
            this.valorAtual += valor;
        }
    }
}

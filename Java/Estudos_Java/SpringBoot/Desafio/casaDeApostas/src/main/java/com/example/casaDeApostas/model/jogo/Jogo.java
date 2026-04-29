package com.example.casaDeApostas.model.jogo;

import com.example.casaDeApostas.model.enums.TipoJogo;
import com.example.casaDeApostas.model.enums.TipoCampo;
import com.example.casaDeApostas.model.users.User;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.boot.webmvc.autoconfigure.WebMvcProperties;

import java.util.*;

@Entity
@Table(name = "Jogos")
@Data
@NoArgsConstructor
public class Jogo {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID idJogo;

    @JsonIgnore
    private TipoCampo[] matriz;

    @ManyToOne
    @JoinColumn(name = "usuario_id")
    @JsonIgnore
    private User usuario;

    private Double valorApostado;

    @JsonIgnore
    private int quantidadeDiamantesEncontrados;

    @JsonIgnore
    @Transient
    private TipoCampo tipoDB;

    @Enumerated(EnumType.STRING)
    private TipoJogo tipoJogo;

    @JsonIgnore
    private int ganhos;

    @JsonIgnore
    private int percas;

    @JsonIgnore
    @Transient
    private Integer linha;

    @JsonIgnore
    @Transient
    private Integer coluna;

    @JsonIgnore
    private Double valorGanho;

    @JsonIgnore
    @Transient
    private Integer quantidadeBombas = 10;


    public Jogo(User usuarioId, Double valorApostado) {
        this.matriz = gerarCampoMinado();
        this.usuario = usuarioId;
        this.valorApostado = valorApostado;
        this.ganhos = 0;
        this.percas = 0;
        this.quantidadeDiamantesEncontrados = 0;
        this.tipoJogo = TipoJogo.EM_ANDAMENTO;
        this.valorGanho = 0.0;
    }

    public Jogo(String mensagem) {
    }

    public TipoCampo[] gerarCampoMinado() {

        matriz = new TipoCampo[25];
        Random random = new Random();

        for (int i = 0; i < matriz.length; i++) {
                matriz[i] = TipoCampo.DIAMANTE;
        }


        for (int i = 0; i < quantidadeBombas; i++){
            matriz[random.nextInt(25)] = TipoCampo.BOMBA;
        }

        return matriz;
    }

    public void adicionarPerdas(int percas) {
        this.percas += percas;
    }

    public void adicionarGanhos(int ganhos) {
        this.ganhos += ganhos;
    }

    public void adicionarDiamantesEncontrados(int aumentarDiamantes){
        this.quantidadeDiamantesEncontrados += aumentarDiamantes;
    }

    public Double calcularGanho(Jogo jogo) {

        double valorGanho = jogo.getValorApostado() * (1 + (jogo.getQuantidadeDiamantesEncontrados() * 0.33));

        jogo.setValorGanho(somarValorGanho(valorGanho));
        return valorGanho;

    }

    private Double somarValorGanho(Double valor){
        return this.valorGanho += valor;
    }


}
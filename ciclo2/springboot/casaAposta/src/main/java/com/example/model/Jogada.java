package com.example.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "jogadas")
public class Jogada {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "aposta_id", nullable = false)
    private Aposta aposta;

    @Column(name = "posicao_x")
    private Integer posicaoX;

    @Column(name = "posicao_y")
    private Integer posicaoY;

    @Column(name = "tipo")
    private String tipo; // DIAMANTE ou BOMBA

    @Column(name = "data_hora")
    private LocalDateTime dataHora = LocalDateTime.now();

    public Jogada() {}

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public Aposta getAposta() { return aposta; }
    public void setAposta(Aposta aposta) { this.aposta = aposta; }

    public Integer getPosicaoX() { return posicaoX; }
    public void setPosicaoX(Integer posicaoX) { this.posicaoX = posicaoX; }

    public Integer getPosicaoY() { return posicaoY; }
    public void setPosicaoY(Integer posicaoY) { this.posicaoY = posicaoY; }

    public String getTipo() { return tipo; }
    public void setTipo(String tipo) { this.tipo = tipo; }

    public LocalDateTime getDataHora() { return dataHora; }
    public void setDataHora(LocalDateTime dataHora) { this.dataHora = dataHora; }
}

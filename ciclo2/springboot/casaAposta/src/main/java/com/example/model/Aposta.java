package com.example.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "apostas")
public class Aposta {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "usuario_id", nullable = false)
    private Usuario usuario;

    @Column(name = "valor_apostado", nullable = false)
    private Double valorApostado;

    @Column(name = "valor_ganho")
    private Double valorGanho;

    @Column(name = "data_hora")
    private LocalDateTime dataHora = LocalDateTime.now();

    @Column(name = "status")
    private String status; // ATIVO, ENCERRADO, ESTOUROU

    @Column(name = "diamantes_encontrados")
    private Integer diamantesEncontrados = 0;

    @Column(name = "tabuleiro")
    private String tabuleiro; // Vamos salvar como JSON string

    public Aposta() {}

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public Usuario getUsuario() { return usuario; }
    public void setUsuario(Usuario usuario) { this.usuario = usuario; }

    public Double getValorApostado() { return valorApostado; }
    public void setValorApostado(Double valorApostado) { this.valorApostado = valorApostado; }

    public Double getValorGanho() { return valorGanho; }
    public void setValorGanho(Double valorGanho) { this.valorGanho = valorGanho; }

    public LocalDateTime getDataHora() { return dataHora; }
    public void setDataHora(LocalDateTime dataHora) { this.dataHora = dataHora; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public Integer getDiamantesEncontrados() { return diamantesEncontrados; }
    public void setDiamantesEncontrados(Integer diamantesEncontrados) { this.diamantesEncontrados = diamantesEncontrados; }

    public String getTabuleiro() { return tabuleiro; }
    public void setTabuleiro(String tabuleiro) { this.tabuleiro = tabuleiro; }
}

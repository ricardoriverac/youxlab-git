package com.example.dto;

import com.example.enuns.PerfilUser;
import com.example.enuns.StatusUser;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;

public class DashboardUserDTO{

    @JsonProperty("id")
    private Long id;

    @JsonProperty("nome")
    private String nome;

    @JsonProperty("email")
    private String email;

    @JsonFormat(pattern = "dd/MM/yyyy")
    @JsonProperty("dataNascimento")
    private LocalDate dataNascimento;

    @JsonProperty("role")
    private PerfilUser role;

    @JsonProperty("status")
    private StatusUser status;

    @JsonProperty("emailConfirmado")
    private Boolean emailConfirmado;

    @JsonProperty("senha")
    private String senha;

    @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
    @JsonProperty("dataCadastro")
    private LocalDateTime dataCadastro;

    @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
    @JsonProperty("ultimoLogin")
    private LocalDateTime ultimoLogin;


    @JsonProperty("totalGanho")
    private BigDecimal totalGanho;

    @JsonProperty("mediaAposta")
    private BigDecimal mediaAposta;

    @JsonProperty("saldo")
    private BigDecimal saldo;

    @JsonProperty("totalDiamantesEncontrados")
    private Long totalDiamantesEncontrados;

    @JsonProperty("totalBombasEncontradas")
    private Long totalBombasEncontradas;

    @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
    @JsonProperty("dataAtualizacao")
    private String dataAtualizacao;

    @JsonProperty("nivelJogador")
    private String nivelJogador;


    public DashboardUserDTO() {
        this.dataAtualizacao = java.time.LocalDateTime.now()
                .format(java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public LocalDate getDataNascimento() { return dataNascimento; }
    public void setDataNascimento(LocalDate dataNascimento) { this.dataNascimento = dataNascimento; }

    public PerfilUser getRole() { return role; }
    public void setRole(PerfilUser role) { this.role = role; }

    public StatusUser getStatus() { return status; }
    public void setStatus(StatusUser status) { this.status = status; }

    public Boolean getEmailConfirmado() { return emailConfirmado; }
    public void setEmailConfirmado(Boolean emailConfirmado) { this.emailConfirmado = emailConfirmado; }

    public String getSenha() { return senha; }
    public void setSenha(String senha) { this.senha = senha; }

    public LocalDateTime getDataCadastro() { return dataCadastro; }
    public void setDataCadastro(LocalDateTime dataCadastro) { this.dataCadastro = dataCadastro; }

    public LocalDateTime getUltimoLogin() { return ultimoLogin; }
    public void setUltimoLogin(LocalDateTime ultimoLogin) { this.ultimoLogin = ultimoLogin; }

    public BigDecimal getTotalGanho() { return totalGanho; }
    public void setTotalGanho(BigDecimal totalGanho) { this.totalGanho = totalGanho; }

    public BigDecimal getMediaAposta() { return mediaAposta; }
    public void setMediaAposta(BigDecimal mediaAposta) { this.mediaAposta = mediaAposta; }

    public BigDecimal getSaldo() { return saldo; }
    public void setSaldo(BigDecimal saldo) { this.saldo = saldo; }

    public Long getTotalDiamantesEncontrados() { return totalDiamantesEncontrados; }
    public void setTotalDiamantesEncontrados(Long totalDiamantesEncontrados) { this.totalDiamantesEncontrados = totalDiamantesEncontrados; }

    public Long getTotalBombasEncontradas() { return totalBombasEncontradas; }
    public void setTotalBombasEncontradas(Long totalBombasEncontradas) { this.totalBombasEncontradas = totalBombasEncontradas; }

    public String getDataAtualizacao() { return dataAtualizacao; }
    public void setDataAtualizacao(String dataAtualizacao) { this.dataAtualizacao = dataAtualizacao; }

    public String getNivelJogador() { return nivelJogador; }
    public void setNivelJogador(String nivelJogador) { this.nivelJogador = nivelJogador; }
}




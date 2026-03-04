package com.example.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String nome;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(name = "data_nascimento", nullable = false)
    private LocalDate dataNascimento;

    @Column(nullable = false)
    private String senha;

    @Column(name = "email_confirmado")
    private Boolean emailConfirmado = false;

    @Column(name = "token_confirmacao")
    private String tokenConfirmacao;

    @Column(name = "token_expiracao")
    private LocalDateTime tokenExpiracao;

    @Column(name = "bloqueado")
    private Boolean bloqueado = false;

    @Column(name = "perfil")
    private String perfil = "USER"; // USER ou ADMIN

    // Construtor vazio (obrigatório para JPA)
    public Usuario() {}

    // Getters e Setters (obrigatórios)
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public LocalDate getDataNascimento() { return dataNascimento; }
    public void setDataNascimento(LocalDate dataNascimento) { this.dataNascimento = dataNascimento; }

    public String getSenha() { return senha; }
    public void setSenha(String senha) { this.senha = senha; }

    public Boolean getEmailConfirmado() { return emailConfirmado; }
    public void setEmailConfirmado(Boolean emailConfirmado) { this.emailConfirmado = emailConfirmado; }

    public String getTokenConfirmacao() { return tokenConfirmacao; }
    public void setTokenConfirmacao(String tokenConfirmacao) { this.tokenConfirmacao = tokenConfirmacao; }

    public LocalDateTime getTokenExpiracao() { return tokenExpiracao; }
    public void setTokenExpiracao(LocalDateTime tokenExpiracao) { this.tokenExpiracao = tokenExpiracao; }

    public Boolean getBloqueado() { return bloqueado; }
    public void setBloqueado(Boolean bloqueado) { this.bloqueado = bloqueado; }

    public String getPerfil() { return perfil; }
    public void setPerfil(String perfil) { this.perfil = perfil; }
}

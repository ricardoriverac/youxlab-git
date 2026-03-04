package com.example.dto;

public class UserResponseDTO {

    private Long id;
    private String nome;
    private String email;
    private LocalDate dataNascimento;
    private Boolean emailConfirmado;
    private String perfil;
    private Boolean bloqueado;

    public UsuarioResponseDTO(Long id, String nome, String email, LocalDate dataNascimento,
                              Boolean emailConfirmado, String perfil, Boolean bloqueado) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.dataNascimento = dataNascimento;
        this.emailConfirmado = emailConfirmado;
        this.perfil = perfil;
        this.bloqueado = bloqueado;
    }

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public LocalDate getDataNascimento() { return dataNascimento; }
    public void setDataNascimento(LocalDate dataNascimento) { this.dataNascimento = dataNascimento; }

    public Boolean getEmailConfirmado() { return emailConfirmado; }
    public void setEmailConfirmado(Boolean emailConfirmado) { this.emailConfirmado = emailConfirmado; }

    public String getPerfil() { return perfil; }
    public void setPerfil(String perfil) { this.perfil = perfil; }

    public Boolean getBloqueado() { return bloqueado; }
    public void setBloqueado(Boolean bloqueado) { this.bloqueado = bloqueado; }
}

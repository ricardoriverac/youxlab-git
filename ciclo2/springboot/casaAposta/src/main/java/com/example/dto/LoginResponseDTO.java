package com.example.dto;

public class LoginResponseDTO {

    private String token;
    private String tipo = "Bearer";
    private String email;
    private String perfil;
    private String nome;

    public LoginResponseDTO(String token, String email, String perfil, String nome) {
        this.token = token;
        this.email = email;
        this.perfil = perfil;
        this.nome = nome;
    }

    // Getters e Setters
    public String getToken() { return token; }
    public void setToken(String token) { this.token = token; }

    public String getTipo() { return tipo; }
    public void setTipo(String tipo) { this.tipo = tipo; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPerfil() { return perfil; }
    public void setPerfil(String perfil) { this.perfil = perfil; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }


}

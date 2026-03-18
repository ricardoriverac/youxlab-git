package com.example.model;



import jakarta.persistence.*;

import java.util.UUID;

@Entity
@Table(name = "reset_senha_tokens")
public class ResetSenhaToken {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String token;

    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    public ResetSenhaToken() {}

    public ResetSenhaToken(User user) {
        this.user = user;
        this.token = gerarToken();
    }



    private String gerarToken() {
        return UUID.randomUUID().toString();
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public User getUser() {
        return user;
    }
}


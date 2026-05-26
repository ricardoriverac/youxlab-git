package com.ProjetinhoSpring1.LojaMusica.loja.entities;

import jakarta.persistence.*;

@Entity
@Table(name = "tb_loja")
public class LojaEntity {

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String id;
    @Column(name = "nome")
    private String nome;
    @Column(name = "localizacao")
    private String localizacao;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getLocalizacao() {
        return localizacao;
    }

    public void setLocalizacao(String localizacao) {
        this.localizacao = localizacao;
    }
}

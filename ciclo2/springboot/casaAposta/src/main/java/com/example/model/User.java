package com.example.model;

import com.example.enuns.PerfilUser;
import com.example.enuns.StatusUser;
import jakarta.persistence.*;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Collection;
import java.util.List;


@Entity
@Table(name = "users")
public class User implements UserDetails {

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

        @Column(name = "token_confirmado")
        private String tokenConfirmado;

        @Column(name = "token_confirmacao")
        private String tokenConfirmacao;

        @Column(name = "ultimo_login")
        private LocalDateTime ultimoLogin;



    @Enumerated(EnumType.STRING)
        @Column(nullable = false)
        private PerfilUser role = PerfilUser.USER;

        @Enumerated(EnumType.STRING)
        @Column(nullable = false)
        private StatusUser status = StatusUser.ATIVO;

        public User() {}

        public User(String nome, String email, LocalDate dataNascimento, String senha) {
            this.nome = nome;
            this.email = email;
            this.dataNascimento = dataNascimento;
            this.senha = senha;
            this.emailConfirmado = false;
            this.role = PerfilUser.USER;
            this.status = StatusUser.PENDENTE;
            this.dataCadastro = LocalDateTime.now();
        }

        @Override
        public Collection<? extends GrantedAuthority> getAuthorities() {   //interface do Spring Security usada para representar as permissões ou papéis (roles) de um usuário.
            if (this.role == PerfilUser.ADMIN) {
                return List.of(new SimpleGrantedAuthority("ROLE_ADMIN"), new SimpleGrantedAuthority("ROLE_USER"));
            } else {
                return List.of(new SimpleGrantedAuthority("ROLE_USER"));
            }
        }

    @Override
    public String getPassword() {
        return "";
    }

    public String getSenha() {
            return this.senha;
        }

    @Override
    public String getUsername() {
            return this.email;
        }

    @Override
    public boolean isAccountNonExpired() {
        return false;
    }

    @Override
    public boolean isAccountNonLocked() {
        return false;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return false;
    }

    @Override
    public boolean isEnabled() {
        return false;
    }

    public LocalDateTime getDataCadastro() {
        return dataCadastro;
    }

    public LocalDateTime getUltimoLogin() {
        return ultimoLogin;
    }

    @Column(name = "data_cadastro")
    public LocalDateTime dataCadastro;

        public void confirmarEmail() {
            this.emailConfirmado = true;
            this.status = StatusUser.ATIVO;
            this.tokenConfirmacao = null;

        }

        public void bloquear() {
            this.status = StatusUser.BLOQUEADO;
        }

        public void desbloquear() {
            this.status = StatusUser.ATIVO;
        }

        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getNome() {
            return nome;
        }

        public void setNome(String nome) {
            this.nome = nome;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public LocalDate getDataNascimento() {
            return dataNascimento;
        }

        public void setDataNascimento(LocalDate dataNascimento) {
            this.dataNascimento = dataNascimento;
        }



        public void setSenha(String senha) {
            this.senha = senha;
        }

        public Boolean getEmailConfirmado() {
            return emailConfirmado;
        }

        public void setEmailConfirmado(Boolean emailConfirmado) {
            this.emailConfirmado = emailConfirmado;
        }

        public String getTokenConfirmacao() {
            return tokenConfirmacao;
        }

        public void setTokenConfirmacao(String tokenConfirmacao) {
            this.tokenConfirmacao = tokenConfirmacao;
        }

        public PerfilUser getRole() {
            return role;
        }

        public void setRole(PerfilUser role) {
            this.role = role;
        }

        public StatusUser getStatus() {
            return status;
        }

        public void setStatus(StatusUser status) {
            this.status = status;
        }


        public void setDataCadastro(LocalDateTime dataCadastro) {
        this.dataCadastro = dataCadastro;

        }

}



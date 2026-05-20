package com.example.casaDeApostas.model.users;

import com.example.casaDeApostas.model.enums.Roles;
import com.example.casaDeApostas.model.jogo.Jogo;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;
import lombok.Data;
import org.jspecify.annotations.Nullable;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.UUID;

@Entity
@Table(name = "users")
@Data
public class User implements UserDetails {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @NotBlank
    private String name;

    @NotBlank
    @Column(unique = true)
    private String email;

    @NotNull
    private LocalDate dataNascimento;

    @NotBlank
    @Size(min = 8)
    @Pattern(regexp = "^(?=.*[A-Z])(?=.*\\d).+$")
    @JsonIgnore
    private String senha;

    @NotNull
    @Enumerated(EnumType.STRING)
    private Roles role;

    @NotNull
    private Long cpf;

    private boolean bloqueado = false;

    public User(String name, String email, LocalDate dataNascimento, String senha, Roles role, Long cpf) {
        this.name = name;
        this.email = email;
        this.dataNascimento = dataNascimento;
        this.senha = senha;
        this.role = role;
        this.cpf = cpf;
    }

    public User(String name, String email, LocalDate dataNascimento, String senha) {
        this.name = name;
        this.email = email;
        this.dataNascimento = dataNascimento;
        this.senha = senha;
    }

    public User(String email, String senha, Roles role){
        this.email = email;
        this.senha = senha;
        this.role = role;
    }

    public User(String senha){
        this.senha = senha;
    }

    public User(String email, String senha) {
        this.email = email;
        this.senha = senha;
    }

    public User() {
    }


    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return List.of(
                new SimpleGrantedAuthority("ROLE_" + role)
        );
    }

    public void setResetarSenha(String senha) {
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
        this.senha = encoder.encode(senha) ;
    }

    @JsonIgnore
    @Override
    public @Nullable String getPassword() {
        return "";
    }

    @JsonIgnore
    @Override
    public String getUsername() {
        return name;
    }

    @JsonIgnore
    @Override
    public boolean isAccountNonExpired() {
        return UserDetails.super.isAccountNonExpired();
    }
    @JsonIgnore
    @Override
    public boolean isAccountNonLocked() {
        return UserDetails.super.isAccountNonLocked();
    }

    @JsonIgnore
    @Override
    public boolean isCredentialsNonExpired() {
        return UserDetails.super.isCredentialsNonExpired();
    }

    @JsonIgnore
    @Override
    public boolean isEnabled() {
        return UserDetails.super.isEnabled();
    }
}

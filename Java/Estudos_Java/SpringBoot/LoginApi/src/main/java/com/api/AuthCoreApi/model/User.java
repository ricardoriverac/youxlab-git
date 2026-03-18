package com.api.AuthCoreApi.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.Data;
import lombok.RequiredArgsConstructor;

@Entity
@Table(name = "login")
@RequiredArgsConstructor
@Data
public class Login {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private String id;

    @Size(min = 15, max = 50)
    @NotBlank
    private String email;

    @Size(min = 2,max = 8)
    @NotBlank
    private String password;

}

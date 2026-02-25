package com.example.Securitypro.controller;

import com.example.Securitypro.domain.user.AuthentaticationDTO;
import com.example.Securitypro.domain.user.ResgisterDTO;
import com.example.Securitypro.domain.user.User;
import com.example.Securitypro.infra.security.TokenService;
import com.example.Securitypro.repositores.UserRepository;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("auth")
public class AuthenticationController {

    private final UserRepository repository;
    private final AuthenticationManager authenticationManager;
    private final TokenService tokenService;
    private final PasswordEncoder passwordEncoder;

    public AuthenticationController(
            UserRepository repository,
            AuthenticationManager authenticationManager,
            TokenService tokenService,
            PasswordEncoder passwordEncoder
    ) {
        this.repository = repository;
        this.authenticationManager = authenticationManager;
        this.tokenService = tokenService;
        this.passwordEncoder = passwordEncoder;
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody @Valid AuthentaticationDTO data) {

        var usernamePassword =
                new UsernamePasswordAuthenticationToken(data.login(), data.password());

        var auth = this.authenticationManager.authenticate(usernamePassword);

        var user = (User) auth.getPrincipal();

        String token = tokenService.generateToken(user);

        return ResponseEntity.ok(Map.of("token", token));
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody @Valid ResgisterDTO data) {

        if (this.repository.findByLogin(data.login()) != null) {
            return ResponseEntity.badRequest().body("Usuário já existe");
        }

        String encryptedPassword = passwordEncoder.encode(data.password());

        User newUser = new User(data.login(), encryptedPassword, data.role());

        this.repository.save(newUser);

        return ResponseEntity.ok("Usuário registrado com sucesso");
    }
}
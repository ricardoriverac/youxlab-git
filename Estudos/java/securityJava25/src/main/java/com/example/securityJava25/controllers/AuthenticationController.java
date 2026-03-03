package com.example.securityJava25.controllers;

import com.example.securityJava25.domain.user.AuthenticationDTO;
import com.example.securityJava25.domain.user.LoginResponseDTO;
import com.example.securityJava25.domain.user.RegisterDTO;
import com.example.securityJava25.domain.user.User;
import com.example.securityJava25.infra.TokenService;
import com.example.securityJava25.repositories.UserRepository;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("auth")
public class AuthenticationController {

    @Autowired
    private AuthenticationManager authenticationManager;
    @Autowired
    private UserRepository repository;
    @Autowired
    private TokenService tokenService;
    @Autowired
    private PasswordEncoder passwordEncoder;
    @PostMapping("/login")
    public ResponseEntity login(@RequestBody @Valid AuthenticationDTO data){
        var usernamePassword = new UsernamePasswordAuthenticationToken(data.login(), data.password());
        var auth = this.authenticationManager.authenticate(usernamePassword);

        var token = tokenService.generateToken((User) auth.getPrincipal());
        return ResponseEntity.ok(new LoginResponseDTO(token));
    }

    @PostMapping("/register")
    public ResponseEntity register(@RequestBody @Valid RegisterDTO data){
    if (this.repository.findByLogin(data.login()) != null) return ResponseEntity.badRequest().build();

    String encryptedPassword = passwordEncoder.encode(data.password());
    User newUser = new User(data.login(), encryptedPassword, data.role());

    this.repository.save(newUser);

    return ResponseEntity.ok().build();
    }

}

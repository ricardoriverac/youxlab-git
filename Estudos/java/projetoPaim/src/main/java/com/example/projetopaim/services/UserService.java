package com.example.projetopaim.services;

import com.example.projetopaim.dtos.UserResponseDTO;
import com.example.projetopaim.entity.User;
import com.example.projetopaim.repositories.UserRepository;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service

public class UserService {
    private final UserRepository repository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository repository, PasswordEncoder passwordEncoder) {
        this.repository = repository;
        this.passwordEncoder = passwordEncoder;
    }

    public void createUser(User user){
        String email = user.getEmail();
        if(repository.findByEmail(user.getEmail()).isPresent()){
            throw new RuntimeException("Caro usuário, este e-mail já possui uma conta vinculada");
        }
        email = email.toLowerCase().trim();
        user.setEmail(email);
        String passwordEncoded = passwordEncoder.encode(user.getPassword());
        user.setPassword(passwordEncoded);
        repository.save(user);
    }

    public List<User> getAll(){
        return repository.findAll();
    }

    public User getByEmail(String email){
        return  repository.findByEmail(email).orElseThrow(() -> new RuntimeException("Caro usuário, este e-mail não tem conta vinculada")));
    }
}

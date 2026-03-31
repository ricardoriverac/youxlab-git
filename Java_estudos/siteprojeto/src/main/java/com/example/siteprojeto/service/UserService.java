package com.example.siteprojeto.service;

import com.example.siteprojeto.dto.LoginDTO;
import com.example.siteprojeto.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.*;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService implements UserDetailsService {

    private final UserRepository repository;

    @Override
    public LoginDTO loadUserByUsername(String login)
            throws UsernameNotFoundException {

        return repository.findByLogin(login)
                .orElseThrow(() ->
                        new UsernameNotFoundException("Usuário não encontrado"));
    }
}
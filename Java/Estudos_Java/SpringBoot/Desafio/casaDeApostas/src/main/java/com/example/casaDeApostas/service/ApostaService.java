package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.LoginDTO;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class ApostaService {

    private final UserRepository userRepository;

    private final TokenService tokenService;

    private final PasswordEncoder passwordEncoder;

    public String login(LoginDTO login) {

        User user = userRepository.findByEmail(login.email());

        if (user == null) {
            return "Erro: Email ou senha incorretos.";
        }

        if (!passwordEncoder.matches(login.senha(), user.getSenha())) {
            return "Erro: Email ou senha incorretos.";
        }

        if (user.isBloqueado()) {
            return "Acesso negado. Usuário bloqueado.";
        }

        else return "Token: " + tokenService.generateTokenUser(user);

    }

}

package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.LoginDTO;
import com.example.casaDeApostas.exceptions.EmailSenhaIncorretos;
import com.example.casaDeApostas.exceptions.UsuaroBloqueado;
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
            throw new EmailSenhaIncorretos("Erro: Email ou senha incorretos.");
        }

        if (!passwordEncoder.matches(login.senha(), user.getSenha())) {
            throw new EmailSenhaIncorretos("Erro: Email ou senha incorretos.");
        }

        if (user.isBloqueado()) {
            throw new UsuaroBloqueado("Acesso negado. Usuário bloqueado.");
        }

        else return "Token: " + tokenService.generateTokenUser(user);

    }

}

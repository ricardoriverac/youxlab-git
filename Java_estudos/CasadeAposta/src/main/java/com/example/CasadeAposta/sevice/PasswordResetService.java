package com.example.CasadeAposta.sevice;


import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.UUID;

@Service
@RequiredArgsConstructor
public class PasswordResetService {

    private final UserRepository userRepository;
    private final EmailService emailService;
    private final PasswordEncoder passwordEncoder;


    public void solicitarReset(String email) {

        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        String token = UUID.randomUUID().toString();

        user.setResetToken(token);
        user.setTokenExpiracao(LocalDateTime.now().plusMinutes(30));

        userRepository.save(user);

        String link = "http://localhost:8080/auth/reset-password/confirm?token=" + token;

        emailService.enviarEmail(
                user.getEmail(),
                "Reset de senha",
                "Clique no link para redefinir sua senha: " + link
        );
    }

    public void resetarSenha(String token, String novaSenha) {

        User user = userRepository.findByResetToken(token)
                .orElseThrow(() -> new RuntimeException("Token inválido"));

        if (user.getTokenExpiracao().isBefore(LocalDateTime.now())) {
            throw new RuntimeException("Token expirado");
        }

        user.setSenha(passwordEncoder.encode(novaSenha));

        user.setResetToken(null);
        user.setTokenExpiracao(null);

        userRepository.save(user);
    }
}
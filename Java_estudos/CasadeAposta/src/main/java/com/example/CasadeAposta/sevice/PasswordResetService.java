package com.example.CasadeAposta.sevice;


import com.example.CasadeAposta.model.PasswordResetToken;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.repositories.ResetTokenRepository;
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
    private final ResetTokenRepository tokenRepository;
    private final EmailService emailService;
    private final PasswordEncoder passwordEncoder;

    public void solicitarReset(String email){

        User user = userRepository.findByEmail(email)
                .orElseThrow();

        String token = UUID.randomUUID().toString();

        PasswordResetToken resetToken = new PasswordResetToken();

        resetToken.setToken(token);
        resetToken.setUsuario(user);
        resetToken.setDataExpiracao(LocalDateTime.now().plusMinutes(30));

        tokenRepository.save(resetToken);

        String link = "http://localhost:8080/auth/reset-password/confirm?token=" + token;

        emailService.enviarEmail(
                user.getEmail(),
                "Reset de senha",
                "Clique no link para redefinir sua senha: " + link
        );
    }

    public void resetarSenha(String token, String novaSenha){

        PasswordResetToken resetToken = tokenRepository.findByToken(token)
                .orElseThrow();

        if(resetToken.isUsado()){
            throw new RuntimeException("Token já utilizado");
        }

        if(resetToken.getDataExpiracao().isBefore(LocalDateTime.now())){
            throw new RuntimeException("Token expirado");
        }

        User user = resetToken.getUsuario();

        user.setSenha(passwordEncoder.encode(novaSenha));

        userRepository.save(user);

        resetToken.setUsado(true);

        tokenRepository.save(resetToken);
    }
}

package com.example.service;

import com.example.model.User;
import com.example.model.ResetSenhaToken;
import com.example.repository.ResetSenhaTokenRepository;
import com.example.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class ResetSenhaService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private ResetSenhaTokenRepository resetSenhaTokenRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;


    public void resetarSenha(String token, String novaSenha) {
        ResetSenhaToken resetToken = resetSenhaTokenRepository.findByToken(token)
                .orElseThrow(() -> new RuntimeException("Token inválido"));

        User user = (User) resetToken.getUser();

        user.setSenha(passwordEncoder.encode(novaSenha));
        userRepository.save(user);

        resetSenhaTokenRepository.delete(resetToken);
    }
}

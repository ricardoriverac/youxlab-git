package com.example.service;


import com.example.dto.LoginRequestDTO;
import com.example.dto.LoginResponseDTO;
import com.example.model.User;
import com.example.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class AuthService {

        @Autowired
        private UserRepository userRepository;

        @Autowired
        private PasswordEncoder passwordEncoder;

        @Autowired
        private TokenService tokenService;


        public LoginResponseDTO autenticar(LoginRequestDTO dados) {
            User user = userRepository.findByEmail(dados.email())
                    .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

            boolean senhaValida = passwordEncoder.matches(dados.senha(), user.getSenha());

            if (!senhaValida) {
                throw new RuntimeException("Senha inválida");
            }

            if (!user.getEmailConfirmado()) {
                throw new RuntimeException("Email não confirmado. Verifique sua caixa de entrada.");
            }

            if (user.getStatus().toString().equals("BLOQUEADO")) {
                throw new RuntimeException("Usuário bloqueado. Entre em contato com o suporte.");
            }

            String token = tokenService.gerarToken(user);
            return new LoginResponseDTO(
                    token,
                    user.getId(),
                    user.getNome(),
                    user.getRole().toString()
            );
        }


    }



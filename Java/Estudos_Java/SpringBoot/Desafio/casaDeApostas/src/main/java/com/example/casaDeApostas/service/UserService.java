package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.LoginDTO;
import com.example.casaDeApostas.dto.UserDTO;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.UserRepository;
import com.example.casaDeApostas.security.SecurityConfiguration;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    private final SecurityConfiguration configuration;

    public void createUsuario(UserDTO user) throws Exception {
        User userRegister = new User(
                user.name(),
                user.email(),
                user.dataNascimento(),
                user.senha(),
                user.role(),
                user.cpf()
        );

        if (userRegister.getSenha().equals(user.confirmacaoSenha())) {
            if (userRepository.existsByEmail(userRegister.getEmail())) {
                throw new Exception("Email já cadastrado!");
            }

            if (userRepository.existsByCpf(userRegister.getCpf())){
                throw new Exception("Cpf já cadastrado!");
            }

            userRegister.setSenha(this.configuration.passwordEncoder().encode(user.senha()));
            userRepository.save(userRegister);
        }
    }

    // Metodo dashborad usuario
}

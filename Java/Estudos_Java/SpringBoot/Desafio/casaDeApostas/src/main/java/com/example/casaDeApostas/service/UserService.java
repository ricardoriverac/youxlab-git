package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.UserDTO;
import com.example.casaDeApostas.exceptions.CpfJaCadastrado;
import com.example.casaDeApostas.exceptions.EmailJaCadastrado;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.JogoRepository;
import com.example.casaDeApostas.repository.UserRepository;
import com.example.casaDeApostas.security.SecurityConfiguration;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    private final SecurityConfiguration configuration;

    public void createUsuario(UserDTO user) {
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
                throw new EmailJaCadastrado("Email já cadastrado!");
            }

            if (userRepository.existsByCpf(userRegister.getCpf())){
                throw new CpfJaCadastrado("Cpf já cadastrado!");
            }

            userRegister.setSenha(this.configuration.passwordEncoder().encode(user.senha()));
            userRepository.save(userRegister);
        }
    }
}

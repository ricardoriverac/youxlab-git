package com.example.service;


import com.example.dto.UserRequestDTO;
import com.example.dto.UserUpdateDTO;
import com.example.enuns.PerfilUser;
import com.example.enuns.StatusUser;
import com.example.model.User;
import com.example.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;


    public User criarUser(UserRequestDTO dados) {
        if (userRepository.existsByEmail(dados.email())) {
            throw new RuntimeException("Email já cadastrado");
        }

        User user = new User();
        user.setNome(dados.nome());
        user.setEmail(dados.email());
        user.setDataNascimento(dados.dataNascimento());

        String senhaCriptografada = passwordEncoder.encode(dados.senha());
        user.setSenha(senhaCriptografada);

        String tokenConfirmacao = UUID.randomUUID().toString();
        user.setTokenConfirmacao(tokenConfirmacao);

        user.setEmailConfirmado(false);
        user.setRole(PerfilUser.USER);
        user.setStatus(StatusUser.PENDENTE);
        user.setDataCadastro(LocalDateTime.now());

        return userRepository.save(user);
    }

    public User criarAdmin(UserRequestDTO dados) {
        User user = new User();
        user.setNome(dados.nome());
        user.setEmail(dados.email());
        user.setDataNascimento(dados.dataNascimento());
        user.setSenha(passwordEncoder.encode(dados.senha()));
        user.setTokenConfirmacao(UUID.randomUUID().toString());
        user.setEmailConfirmado(true);
        user.setRole(PerfilUser.ADMIN);
        user.setStatus(StatusUser.ATIVO);
        user.setDataCadastro(LocalDateTime.now());

        return userRepository.save(user);
    }


    public User confirmarEmail(String token) {
        User user = userRepository.findByTokenConfirmacao(token)
                .orElseThrow(() -> new RuntimeException("Token de confirmação inválido"));

        user.confirmarEmail();
        return userRepository.save(user);
    }


    public User buscarPorId(Long id) {
        return userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));
    }


    public List<User> listarTodos() {
        return userRepository.findAll();
    }

    public List<User> listarPorStatus(String status) {
        try {
            StatusUser statusEnum = StatusUser.valueOf(status.toUpperCase());
            return userRepository.findByStatus(statusEnum);
        } catch (IllegalArgumentException e) {
            throw new RuntimeException("Status inválido. Use: ATIVO, BLOQUEADO ou PENDENTE");
        }
    }

    public List<User> listarBloqueados() {
        return userRepository.findByStatus(StatusUser.BLOQUEADO);
    }

    public List<User> listarPendentes() {
        return userRepository.findByStatus(StatusUser.PENDENTE);
    }


    public User atualizarUser(Long id, UserUpdateDTO dados) {
        System.out.println("entoru");
        User user = buscarPorId(id);
        System.out.println("instanciou um usuário do banco");

        if (dados.nome() != null && !dados.nome().isEmpty()) {
            user.setNome(dados.nome());
        }
        System.out.println("passou pelo nome");
        if (dados.email() != null && !dados.email().isEmpty()) {
            userRepository.findByEmail(dados.email()).ifPresent(emailExistente -> {
                if (!emailExistente.getId().equals(id)) {
                    throw new RuntimeException("Email já está em uso por outro usuário");
                }
            });
            user.setEmail(dados.email());
        }
        System.out.println("passou pelo email");
        if (dados.dataNascimento() != null) {
            user.setDataNascimento(dados.dataNascimento());
        }
        System.out.println("passou pela data");
        return userRepository.save(user);
    }

    public void bloquearUser(Long id) {
        User user = buscarPorId(id);
        user.bloquear();
        userRepository.save(user);
    }

    public void desbloquearUser(Long id) {
        User user = buscarPorId(id);
        user.desbloquear();
        userRepository.save(user);
    }



    public void deletarUser(Long id) {
        User user = buscarPorId(id);
        userRepository.delete(user);
    }

    public void validarEmailExistente(String email) {
        if (userRepository.existsByEmail(email)) {
            throw new RuntimeException("Email já cadastrado");
        }
    }


}


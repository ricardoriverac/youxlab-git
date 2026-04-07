package com.example.CasadeAposta.service;

import com.example.CasadeAposta.dtos.AuthDTO;
import com.example.CasadeAposta.dtos.UserDTO;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.util.List;
import java.util.UUID;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public List<User> listarUsuarios() {
        return userRepository.findAll();
    }


    public User buscarPorId(UUID id) {
        return userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));
    }


    public UserDTO registrar(AuthDTO dto){

        if(userRepository.findByEmail(dto.email()).isPresent()){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "Email já cadastrado");
        }

        User user = new User();

        user.setNome(dto.nome());
        user.setEmail(dto.email());
        user.setDataNascimento(dto.dataNascimento());
        user.setSenha(passwordEncoder.encode(dto.senha()));
        user.setPapel(dto.role());

        user = userRepository.save(user);

        return new UserDTO(
                user.getNome(),
                user.getEmail()
        );
    }


    public User atualizar(UUID id, User dados) {
        User user = buscarPorId(id);

        if (dados.getNome() != null) {
            user.setNome(dados.getNome());
        }

        if (dados.getEmail() != null) {
            user.setEmail(dados.getEmail());
        }

        return userRepository.save(user);
    }


    public User bloquear(UUID id) {
        User user = buscarPorId(id);
        user.setAtivo(false);
        return userRepository.save(user);
    }

    public User ativar(UUID id) {
        User user = buscarPorId(id);
        user.setAtivo(true);
        return userRepository.save(user);
    }
}
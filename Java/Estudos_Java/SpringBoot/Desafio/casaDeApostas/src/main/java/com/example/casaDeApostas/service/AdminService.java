package com.example.casaDeApostas.service;

import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.beans.NullValueInNestedPathException;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class AdminService {

    private final UserRepository userRepository;

    public List<User> allUsers(){

        return userRepository.findAll();
    }

    public User getByCpf(Long cpf) {
        return userRepository.findByCpf(cpf);
    }

    public String blockUser(Long cpf) {

        User user = userRepository.findByCpf(cpf);

        user.setBloqueado(true);
        userRepository.save(user);
        return "Usuário bloqueado com sucesso.";
    }

    public String unlockUser(Long cpf) {

        User user = userRepository.findByCpf(cpf);

        user.setBloqueado(false);
        userRepository.save(user);
        return "Usuário bloqueado com sucesso.";
    }
    // metodo dashboard admin
}

package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.AdminDTO;
import com.example.casaDeApostas.model.enums.Roles;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.AccountRepository;
import com.example.casaDeApostas.repository.UserRepository;
import com.example.casaDeApostas.security.SecurityConfiguration;
import lombok.AllArgsConstructor;
import org.springframework.beans.NullValueInNestedPathException;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class AdminService {

    private final UserRepository userRepository;

    public List<User> allUsers(){
        try {
            return userRepository.findAll();
        }
        catch (NullValueInNestedPathException e){
            throw new RuntimeException("Nenhum usuário cadastrado.", e);
        }
    }

    public User getByCpf(Long cpf) {
        User user = new User();
        user = userRepository.findByCpf(cpf);

        return user;

    }

    // metodo para bloquear


    // metodo dashboard admin
}

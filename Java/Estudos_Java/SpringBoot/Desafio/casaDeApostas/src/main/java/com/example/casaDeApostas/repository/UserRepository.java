package com.example.casaDeApostas.repository;

import com.example.casaDeApostas.model.enums.Roles;
import com.example.casaDeApostas.model.users.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface UserRepository extends JpaRepository<User, UUID> {

    boolean existsByEmail(String email);
    boolean existsByCpf(Long cpf);

    User findByEmail(String email);

    User findByCpf(Long cpf);
}

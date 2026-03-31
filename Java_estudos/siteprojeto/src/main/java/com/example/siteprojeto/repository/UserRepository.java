package com.example.siteprojeto.repository;

import com.example.siteprojeto.dto.LoginDTO;
import com.example.siteprojeto.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;
import java.util.UUID;

public interface UserRepository extends JpaRepository<User, UUID> {
    Optional<LoginDTO> findByLogin(String login);
}
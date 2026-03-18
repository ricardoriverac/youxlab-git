package com.example.CasadeAposta.repositories;

import com.example.CasadeAposta.model.Aposta;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.model.enums.ApostaStatus;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface ApostaRepository extends JpaRepository<Aposta, UUID> {

    Optional<Aposta> findByUsuarioAndStatus(User usuario, ApostaStatus status);
}
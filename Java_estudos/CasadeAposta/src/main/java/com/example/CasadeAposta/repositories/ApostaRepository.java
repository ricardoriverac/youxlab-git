package com.example.CasadeAposta.repositories;

import com.example.CasadeAposta.model.Aposta;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.model.enums.ApostaStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.math.BigDecimal;
import java.util.Optional;
import java.util.UUID;

public interface ApostaRepository extends JpaRepository<Aposta, UUID> {

    Optional<Aposta> findByUsuarioAndStatus(User usuario, ApostaStatus status);

    @Query("SELECT SUM(a.valorGanhos) FROM Aposta a WHERE a.status = 'FINALIZADA'")
    BigDecimal totalGanhos();

    long countByStatus(ApostaStatus status);

    long countByUsuario(User user);

    long countByUsuarioAndStatus(User user, ApostaStatus status);

}
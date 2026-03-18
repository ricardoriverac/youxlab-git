package com.example.repository;

import com.example.model.ResetSenhaToken;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ResetSenhaTokenRepository  extends JpaRepository<ResetSenhaToken, Long> {

    Optional<ResetSenhaToken> findByToken(String token);

}

package com.example.casaDeApostas.repository;


import com.example.casaDeApostas.model.jogo.Jogo;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface JogoRepository extends JpaRepository<Jogo, UUID> {
}

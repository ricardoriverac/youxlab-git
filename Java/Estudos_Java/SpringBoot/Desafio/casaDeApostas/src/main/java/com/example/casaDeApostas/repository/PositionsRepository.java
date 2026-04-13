package com.example.casaDeApostas.repository;

import com.example.casaDeApostas.model.position.Positions;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface PositionsRepository extends JpaRepository<Positions, UUID> {
}

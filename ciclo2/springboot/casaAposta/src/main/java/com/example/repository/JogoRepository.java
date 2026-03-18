package com.example.repository;

import com.example.enuns.StatusJogo;
import com.example.model.Jogo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;

public interface JogoRepository extends JpaRepository<Jogo, Long> {



        Optional<Jogo> findByUserIdAndStatus(Long userId, StatusJogo status);

        Long countByUserId(Long userId);

        @Query("SELECT COALESCE(SUM(j.valorGanho), 0) FROM Jogo j WHERE j.user.id = :userId AND j.status IN ('GANHOU', 'ENCERRADO')")
        BigDecimal somarValorGanhoPorUser(@Param("userId") Long userId);

        @Query("SELECT COALESCE(SUM(j.valorGanho), 0) FROM Jogo j WHERE j.status IN ('GANHOU', 'ENCERRADO')")
        BigDecimal somarValorGanhoTotal();


        @Query("SELECT MAX(j.valorGanho) FROM Jogo j WHERE j.user.id = :userId AND j.status IN ('GANHOU', 'ENCERRADO')")
        BigDecimal encontrarMaiorGanhoPorUser(@Param("userId") Long userId);

        @Query("SELECT MAX(j.valorGanho) FROM Jogo j WHERE j.status IN ('GANHOU', 'ENCERRADO')")
        BigDecimal encontrarMaiorGanhoTotal();

        @Query("SELECT AVG(j.valorAposta) FROM Jogo j WHERE j.user.id = :userId")
        Double calcularMediaApostaPorUser(@Param("userId") Long userId);


        List<Jogo> findTop10ByOrderByDataInicioDesc();


    }


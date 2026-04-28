package com.example.casaDeApostas.repository;


import com.example.casaDeApostas.model.jogo.Jogo;
import com.example.casaDeApostas.model.users.User;
import jakarta.persistence.criteria.CriteriaBuilder;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;
import java.util.UUID;

public interface JogoRepository extends JpaRepository<Jogo, UUID> {

    @Query("""
        SELECT SUM(valorGanho) FROM Jogo""")
    Double ValorCadaPartida();

    Long countJogoByUsuario_Id(UUID usuarioId);

    @Query("SELECT SUM(j.ganhos) FROM Jogo j WHERE j.usuario.id = :idUser")
    Integer contarGanhosPorUsuario(UUID idUser);

    @Query("SELECT SUM(j.percas) FROM Jogo j WHERE j.usuario.id = :idUser")
    Integer contarPercasPorUsuario(UUID idUser);

    @Query("SELECT COUNT(*) FROM Jogo")
    Long countAll();
}

package com.example.repository;

import com.example.enuns.TipoCelula;
import com.example.model.Jogada;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;


public interface JogadaRepository extends JpaRepository<Jogada, Long> {

        Long countByUserIdAndTipoCelula(Long userId, TipoCelula tipoCelula);

        @Query("SELECT COUNT(j) FROM Jogada j WHERE j.user.id = :userId AND j.tipoCelula IN ('DIAMANTE', 'DIAMANTE_VITORIA')")
        Long countDiamantesByUserId(@Param("userId") Long userId);


        @Query("SELECT COUNT(j) > 0 FROM Jogada j WHERE j.jogo.id = :jogoId AND j.linha = :linha AND j.coluna = :coluna")
        boolean existsByJogoIdAndPosicao(@Param("jogoId") Long jogoId, @Param("linha") Integer linha, @Param("coluna") Integer coluna);

}


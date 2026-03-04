package com.example.repository;

public interface JogadaRepository extends JpaRepository<Jogada, Long>{

    List<Jogada> findByAposta(Aposta aposta);
    boolean existsByApostaAndPosicaoXAndPosicaoY(Aposta aposta, Integer x, Integer y);
}

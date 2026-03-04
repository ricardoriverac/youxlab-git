package com.example.repository;

public interface ApostaRepository extends JpaRepository<Aposta, Long>{

    List<Aposta> findByUsuario(Usuario usuario);
    Optional<Aposta> findByIdAndUsuario(Long id, Usuario usuario);
    List<Aposta> findByUsuarioAndStatus(Usuario usuario, String status);

    @Query("SELECT COUNT(a) FROM Aposta a")
    Long countTotalApostas();

    @Query("SELECT COALESCE(SUM(a.valorApostado), 0) FROM Aposta a WHERE a.status = 'ESTOUROU'")
    Double somaGanhoCasa();

    @Query("SELECT COALESCE(SUM(a.valorGanho), 0) FROM Aposta a WHERE a.status = 'ENCERRADO'")
    Double somaPagoUsuarios();
}

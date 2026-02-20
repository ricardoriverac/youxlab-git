package com.example.librayapi.repository;

import com.example.librayapi.model.Autor;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface AutorRepository extends JpaRepository<Autor, UUID> {

    List<Autor> findByNome(String nome);
    List<Autor> findByNomeAndNacionalidade(String nome, String nacionalidade);
    List<Autor> findByNacionalidade(String nacionalidade);

    Optional<Autor> findByNomeAndDataNascimentoAndNacionalidade(
            String nome , LocalDate data_nascimento, String nacionalidade
    );


}

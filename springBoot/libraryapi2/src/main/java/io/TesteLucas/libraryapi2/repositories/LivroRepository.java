package io.TesteLucas.libraryapi2.repositories;

import io.TesteLucas.libraryapi2.model.Autor;
import io.TesteLucas.libraryapi2.model.Livro;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface LivroRepository extends JpaRepository<Livro, UUID> {

    boolean existsByAutor(Autor autor);

    List<Livro> findByAutor(Autor autor);
}

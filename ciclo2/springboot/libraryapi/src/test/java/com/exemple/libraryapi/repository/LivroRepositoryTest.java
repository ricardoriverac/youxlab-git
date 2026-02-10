package com.exemple.libraryapi.repository;

import com.exemple.libraryapi.model.Autor;
import com.exemple.libraryapi.model.GeneroLivro;
import com.exemple.libraryapi.model.Livro;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.UUID;

import static org.postgresql.core.JavaVersion.other;

@SpringBootTest
class LivroRepositoryTest {

    @Autowired
    LivroRepository repository;

    @Autowired
    AutorRepository autorRepository;

    @Test
    void salvarTest() {
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Outro livro");
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        Autor autor = autorRepository.
        findById(UUID.fromString("76e7c418-ccf9-4e2a-af20-c28b9e50ab55"))
        .orElse(null);


        livro.setAutor(autor);

        repository.save(livro);

    }

    @Test
    void salvarCascadeTest(){
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero (GeneroLivro.FICCAO);
        livro.setTitulo ("Outro Livro");
        livro.setDataPublicacao (LocalDate.of(1980, 1, 2));

        Autor autor = new Autor();
        autor.setNome("João");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento (LocalDate.of (1951, 1 ,  31));

        autorRepository.save(autor);

        livro.setAutor (autor);

        repository.save(livro);
    }
}

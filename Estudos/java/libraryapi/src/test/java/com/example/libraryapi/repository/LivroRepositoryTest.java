package com.example.libraryapi.repository;

import com.example.libraryapi.model.Autor;
import com.example.libraryapi.model.Livro;
import com.example.libraryapi.model.enums.GeneroLivro;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.UUID;

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
        livro.setTitulo("Outro Livro");
        livro.setData_publicacao(LocalDate.of(1980, 1, 2));

        Autor autor = autorRepository.findById(UUID.fromString("a339b8e0-c5b2-4102-9d73-b60dcc7482e2")).orElse(null);

        livro.setAutor(new Autor());

        repository.save(livro);
    }

    @Test
    void salvarAutorELivroTest() {
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Terceiro Livro");
        livro.setData_publicacao(LocalDate.of(1980, 1, 2));

        Autor autor = new Autor();
        autor.setNome("José");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        autorRepository.save(autor);

        livro.setAutor(autor);

        repository.save(livro);

    }

    @Test
    void salvarCascadeTest() {
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Outro Livro");
        livro.setData_publicacao(LocalDate.of(1980, 1, 2));

        Autor autor = new Autor();
        autor.setNome("João");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        livro.setAutor(autor);

        repository.save(livro);
    }

    @Test
    void atualizarAutorDoLivro()
    {
        var livroParaAtualizar = repository.findById(UUID.fromString("5d81c614-b452-4cff-8ced-1052d87f2809")).orElse(null);

        UUID idAutor = UUID.fromString("4fab456f-61d9-4039-94bd-8e402aab97dc");
        Autor joão = autorRepository.findById(idAutor).orElse(null);

        livroParaAtualizar.setAutor(joão);

        repository.save(livroParaAtualizar);

    }

    @Test
    void deletar(){
        UUID id = UUID.fromString("4fab456f-61d9-4039-94bd-8e402aab97dc");
        repository.deleteById(id);
    }

    @Test
    void deletarCascade(){
        UUID id = UUID.fromString("0358a37b-c921-4932-af62-55d41c35470f");
        repository.deleteById(id);
    }

    @Test
    @Transactional
    void buscarLivroTest(){
        UUID id = UUID.fromString("5d81c614-b452-4cff-8ced-1052d87f2809");
        Livro livro = repository.findById(id).orElse(null);
        System.out.println("Livro: ");
        System.out.println(livro.getTitulo());

        System.out.println("Autor: ");
        System.out.println(livro.getAutor().getNome());
    }
}
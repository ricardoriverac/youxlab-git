package com.example.librayapi.repository;

import com.example.librayapi.model.Autor;
import com.example.librayapi.model.GeneroLivro;
import com.example.librayapi.model.Livro;
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
    void salvarTest(){

        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("UFO");
        livro.setDataPublicacao(LocalDate.of(1980, 1,2));

        Autor autor = autorRepository
                .findById(UUID.fromString("6da6480f-a656-42b2-89fe-fd88c41be534"))
                .orElse(null);

        livro.setAutor(autor);
        repository.save(livro);
    }

    @Test
    void salvarCascadeTest(){

        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("UFO");
        livro.setDataPublicacao(LocalDate.of(1980, 1,2));

        Autor autor = new Autor();
        autor.setNome("Joao");
        autor.setNascionalidade("Brasileira");
        autor.setData_nascimento(LocalDate.of(1951, 1, 31));

        livro.setAutor(autorRepository.save(autor));
        repository.save(livro);
    }

    @Test
    void salvarAutorLivroTest(){
        UUID id = UUID.fromString("c91d8f02-6b73-41ff-ac64-6b7ac84eebcc");
        Livro livroParaAtualizar = repository.findById(id).orElse(null);

        UUID idautor= UUID.fromString("6da6480f-a656-42b2-89fe-fd88c41be534");
        Autor autor = autorRepository.findById(idautor).orElse(null);

        livroParaAtualizar.setAutor(autor);
        repository.save(livroParaAtualizar);

    }

    @Test
    void deletar(){
        UUID id = UUID.fromString("0c54d8c0-b714-439c-96a9-fad537b74ad1");
        repository.deleteById(id);



    }


    @Test
    @Transactional
    void buscarLivroTest(){
        UUID id = UUID.fromString("5f679192-b79e-40db-a839-08788ec0c6f2");
        Livro livro = repository.findById(id).orElse(null);
        System.out.println("Livro: ");
        System.out.println(livro.getTitulo());
        System.out.println("Autor: ");
        System.out.println(livro.getAutor().getNome());
    }

    @Test
    void deletePorGenero(){
        repository.deleteByGenero(GeneroLivro.CIENCIA);
    }

    @Test
    void updateDataPublicacapTest(){
        repository.uppdateDataPublicacao(LocalDate.of(2000, 9,2));
    }
}
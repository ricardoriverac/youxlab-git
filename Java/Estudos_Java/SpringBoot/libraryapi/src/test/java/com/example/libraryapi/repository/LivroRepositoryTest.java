package com.example.libraryapi.repository;

import com.example.libraryapi.model.Autor;
import com.example.libraryapi.model.GeneroLivro;
import com.example.libraryapi.model.Livro;
import jakarta.transaction.Transactional;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;
import java.util.Optional;
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
        livro.setGenero(GeneroLivro.CIENCIA);
        livro.setTitulo("Ciencias");
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        Autor autor = autorRepository
                .findById(UUID.fromString("e48f9040-6db7-4958-acfb-0bec777566ed"))
                .orElse(null);

        livro.setAutor(autor);
        repository.save(livro);
    }

    @Test
    void salvarAutorELivroTest(){
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Terceiro Livro");
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        Autor autor = new Autor();
        autor.setNome("José");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        autorRepository.save(autor);

        livro.setAutor(autor);
        repository.save(livro);
    }

    @Test
    void salvarCascadeTest(){
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Outro Livro");
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        Autor autor = new Autor();
        autor.setNome("João");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        livro.setAutor(autor);
        repository.save(livro);
    }

    @Test
    void atualizarAutorDoLivro(){
       UUID id = UUID.fromString("c8cc05b8-2edd-4404-bf83-547715834276");
       var livroParaAtualizar = repository.findById(id).orElse(null);

       UUID idAutor = UUID.fromString("0b5803fe-f44e-4bd7-b37a-fa0d06a7d43c");
       Autor maria = autorRepository.findById(idAutor).orElse(null);

       livroParaAtualizar.setAutor(maria);

       repository.save(livroParaAtualizar);
    }

    @Test
    void deletar(){
        UUID id = UUID.fromString("c8cc05b8-2edd-4404-bf83-547715834276");
        repository.deleteById(id);
    }

    @Test
    void deletarCascade(){
        UUID id = UUID.fromString("b57df0ac-bcd9-46b7-b7fe-0dc17bfc7d4c");
        repository.deleteById(id);
    }

    @Test
    @Transactional
    void buscarLivroTest(){
        UUID id = UUID.fromString("19317c93-6f0a-4757-8f52-1f9a2ac42135");
        Livro livro = repository.findById(id).orElse(null);
        System.out.println("LIVRO:");
        System.out.println(livro.getTitulo());

//        System.out.println("AUTOR:");
//        System.out.println(livro.getAutor().getNome());

    }

    @Test
    void pesquisaPorTituloTest(){
        List<Livro> lista = repository.findByTitulo("O roubo da casa assombrada");
        lista.forEach(System.out::println);
    }

    @Test
    void pesquisaPorISBNest(){
        List<Livro> lista = repository.findByIsbn("20847-84874");
        lista.forEach(System.out::println);
    }

    @Test
    void pesquisaPorTituloEPrecoTest(){
        var preco = BigDecimal.valueOf(204.00);

        var tituloPesquisa = "O roubo da casa assombrada";
        List<Livro> lista = repository.findByTituloAndPreco(tituloPesquisa, preco);
        lista.forEach(System.out::println);
    }

    @Test
    void listarLivrosComQueryJPQL(){
        var resultado = repository.listarTodosOrdenadoPorTituloAndPreco();
        resultado.forEach(System.out::println);
    }

    @Test
    void listarAutoresDosLivros(){
        var resultado = repository.listarAutoresDosLivro();
        resultado.forEach(System.out::println);
    }

    @Test
    void listarTitulosNaoRepetidosDosLivros(){
        var resultado = repository.listarNomesDiferentesLivros();
        resultado.forEach(System.out::println);
    }

    @Test
    void listarGeneroDeLivrosAutoresBrasileiros(){
        var resultado = repository.listarGenerosAutoresBrasileiros();
        resultado.forEach(System.out::println);
    }

    @Test
    void listarPorGeneroQueryParamTest(){
        var resultado = repository.findByGenero(GeneroLivro.MISTERIO, "dataPublicacao");
        resultado.forEach(System.out::println);
    }

    @Test
    void listarPorGeneroPositionalParamTest(){
        var resultado = repository.findByGeneroPositionalParammeters(GeneroLivro.MISTERIO, "dataPublicacao");
        resultado.forEach(System.out::println);
    }

    @Test
    void deletePorGeneroTest(){
        repository.deleteByGenero(GeneroLivro.CIENCIA);
    }

    @Test
    void updateDataPublicacaoTest(){
        repository.updateDataPublicacao(LocalDate.of(2000, 1, 1));
    }

}
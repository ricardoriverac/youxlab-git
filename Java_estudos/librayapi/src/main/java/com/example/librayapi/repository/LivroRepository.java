package com.example.librayapi.repository;

import com.example.librayapi.model.Autor;
import com.example.librayapi.model.GeneroLivro;
import com.example.librayapi.model.Livro;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;
import java.util.UUID;

public interface LivroRepository extends JpaRepository<Livro, UUID> {

    List<Livro> findByAutor(Autor autor);

    List<Livro> findByTitulo(String titulo);

    List<Livro> findByIsbn(String isbn);

    List<Livro> findByTituloAndPreco(String titulo, BigDecimal preco);

    List<Livro> findByTituloOrIsbn(String titulo, String isbn);

    List<Livro> findByTituloOrIsbnOrderby(String titulo, String isbn);

    List<Livro> findByDataPublicacaoBetween(LocalDate inicio, LocalDate fim);

    @Query("select l from Livro as l order by l.titulo, l.preco ")
    List<Livro> listarTodosOrdenadosPorTituloAndPreco();

    @Query("select a from Livro l join l.autor")
    List<Autor> listarAutoresDosLivros();

    @Query("select l from Livro l where l.genero  =:nomeDoParametro")
    List<Livro> findByGenero(@Param("nomeDoParametro")GeneroLivro generoLivro);


    @Modifying
    @Transactional
    @Query("delete from Livro where genero = ?1 ")
    void deleteByGenero(GeneroLivro generoLivro);



    @Modifying
    @Transactional
    @Query("update Livro set dataPublicacao = ?1 ")
    void uppdateDataPublicacao(LocalDate novaData);

}

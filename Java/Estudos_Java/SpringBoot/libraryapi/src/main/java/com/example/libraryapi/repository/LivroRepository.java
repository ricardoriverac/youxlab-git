package com.example.libraryapi.repository;

import com.example.libraryapi.model.Autor;
import com.example.libraryapi.model.GeneroLivro;
import com.example.libraryapi.model.Livro;
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

    // Query method
    // select * from livro where id_autor = id
    List<Livro> findByAutor(Autor autor);

    // select * from livro where titulo = titulo
    List<Livro> findByTitulo(String titulo);

    // select * from livro where isbn = isbn
    List<Livro> findByIsbn(String isbn);

    // select * from livro where titulo = ? and preco = ?
    List<Livro> findByTituloAndPreco(String titulo, BigDecimal preco);

    // select * from livro where titulo = ? or isbn = ?
    List<Livro> findByTituloOrIsbnOrderByTitulo(String titulo, String isbn);

    // select * from livro where data_publicacao between ? and ?
    List<Livro> findByDataPublicacaoBetween(LocalDate inicio, LocalDate fim);

    // JPQL -> referencia as entidades e as propriedades da entidade
    // select l.* from Livro as l order by l.titulo
    @Query(" select l from Livro as l order by l.titulo, l.preco ")
    List<Livro> listarTodosOrdenadoPorTituloAndPreco();

    //select a.*
    //from livro l
    //join autor as a on a.id = l.id_autor
    @Query(" select a from Livro l join l.autor a ")
    List<Autor> listarAutoresDosLivro();

    // select distinct l.* from Livro l
    @Query(" select distinct l.titulo from Livro l ")
    List<String> listarNomesDiferentesLivros();

    @Query("""
        select l.genero
        from Livro l 
        join l.autor a
        where a.nacionalidade = 'Brasileira'
        order by l.genero  
      """)
    List<String> listarGenerosAutoresBrasileiros();

    // named parameters -> parametros nomeados
    @Query(" select l from Livro l where l.genero = :genero order by  :paramOrdenacao")
    List<Livro> findByGenero(
            @Param("genero") GeneroLivro generoLivro,
            @Param("paramOrdenacao") String nomePropriedade
    );

    // positional parameters
    @Query(" select l from Livro l where l.genero = ?1 order by ?2 ")
    List<Livro> findByGeneroPositionalParammeters(GeneroLivro generoLivro, String nomePropriedade);

    @Modifying
    @Transactional
    @Query(" delete from Livro where genero = ?1 ")
    void deleteByGenero(GeneroLivro genero);

    @Modifying
    @Transactional
    @Query(" update Livro set dataPublicacao = ?1 ")
    void updateDataPublicacao(LocalDate novaData);

    boolean existsByAutor(Autor autor);
}

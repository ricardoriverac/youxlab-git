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

@SpringBootTest
public class TransacoesTest {
    @Autowired
    AutorRepository autorRepository;

    @Autowired
    private LivroRepository livroRepository;


    @Test
    @Transactional
    void transacaoSimples(){

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

        if (autor.getNome().equals("Joao")){
            throw new RuntimeException("Rollback!");
        }
        livroRepository.save(livro);
}
}

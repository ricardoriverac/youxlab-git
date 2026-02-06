package com.example.libraryapi.service;

import com.example.libraryapi.model.Autor;
import com.example.libraryapi.model.Livro;
import com.example.libraryapi.model.enums.GeneroLivro;
import com.example.libraryapi.repository.AutorRepository;
import com.example.libraryapi.repository.LivroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.UUID;

@Service
public class TransacaoService {
    @Autowired
    private AutorRepository autorRepository;

    @Autowired
    private LivroRepository livroRepository;

    @Transactional
    public void salvarLivroComFoto(){

    }

    @Transactional
    public void atualizacaoSemAtualizar(){
        var livro = livroRepository.findById(UUID.fromString("bfccbc0b-4e39-43a4-8d95-586f33c2021d")).orElse(null);
        livro.setDataPublicacao(LocalDate.of(2024, 6, 1));
    }


    @Transactional
    public void executar(){

        Autor autor = new Autor();
        autor.setNome("José");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        autorRepository.save(autor);



        autorRepository.save(autor);


        Livro livro = new Livro();
        livro.setIsbn("90887-8474");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Teste livro do francisco");
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        livro.setAutor(autor);


        
    }


}

package com.exemple.libraryapi.service;

import com.exemple.libraryapi.model.Autor;
import com.exemple.libraryapi.model.GeneroLivro;
import com.exemple.libraryapi.model.Livro;
import com.exemple.libraryapi.repository.AutorRepository;
import com.exemple.libraryapi.repository.LivroRepository;
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

    /// livro (titulo.... nome_arquivo) -> id.png
    @Transactional
    public void salvarLivroComFoto() {
        // salva o Livro
        //repository.save(Livno);

        // pega o id do Livro livro.getId();
        // var id livro.getId();

        // salvar foto do Livro bucket na nuvem
        // bucketService.salvar(Livro.getFoto(), id + ".png");

        // atualizar o nome arquivo que foi salvo
        // Livro.setNomeArquivoFoto(id.png");
    }

    @Transactional
    public void atualizacaoSemAtualizar(){
        var livro = livroRepository.findById(UUID.fromString("54700b21-26b4-46bd-bdcf-c28825ebe43c")).
                orElse(null);

        livro.setDataPublicacao(LocalDate.of(2024, 6, 1));
    }

    @Transactional
    public void executar(){
        // salvar o autor
        Autor autor = new Autor();
        autor.setNome("Teste Francisco");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        autorRepository.save(autor);

        // salvar o livro
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Teste Livro de Francisco ");
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        livro.setAutor(autor);

        livroRepository.save(livro);

        if(autor.getNome().equals("Teste Francisco")){
            throw new RuntimeException("RollBack!");
        }
    }

}

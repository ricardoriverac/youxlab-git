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
                findById(UUID.fromString("0d3dbd7c-d544-4a5e-9d78-13fc986c6bb6"))
                .orElse(null);


        livro.setAutor(autor);

        repository.save(livro);

    }

    @Test
    void salvarAutorELivroTest() {
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Outro Livro");
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
    void salvarCascadeTest() {
        Livro livro = new Livro();
        livro.setIsbn("90887-84874");
        livro.setPreco(BigDecimal.valueOf(100));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("Terceiro livro");
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        Autor autor = new Autor();
        autor.setNome("João");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        autorRepository.save(autor);

        livro.setAutor(autor);

        repository.save(livro);
    }

    @Test
    void atualizarAutorDoLivro(){
        UUID id = UUID.fromString("6f2d079b-c80c-4fc8-bbb8-ac174c18825e");
        var livroParaAtualizar = repository.findById(id).orElseThrow();

        UUID idAutor = UUID.fromString("1cca68c5-88f8-495d-8d0f-18b33aa83e3f");
        Autor maria = autorRepository.findById(idAutor).orElseThrow();

        livroParaAtualizar.setAutor(maria);

        repository.save (livroParaAtualizar);
    }

    @Test
    void deletar(){
        UUID id = UUID.fromString("e649f7f2-42fe-4511-8940-ab3063e393af");
        repository.deleteById(id);
    }

    @Test
    void deletarCascade(){
        UUID id = UUID.fromString("001167ca-9157-44c9-9416-fb264af215a4");
        repository.deleteById(id);
    }

    @Test
    void buscarLivroTest(){
        UUID id= UUID.fromString("daed83b3-65fd-49eb-9400-cbc0af13659d");
        Livro livro = repository.findById(id).orElse (null);
        System.out.println("Livro: ");
        System.out.println(livro.getTitulo());

        System.out.println("Autor: ");
        System.out.println(livro.getAutor().getNome());
    }


}

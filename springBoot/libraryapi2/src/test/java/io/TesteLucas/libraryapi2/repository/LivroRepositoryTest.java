package io.TesteLucas.libraryapi2.repository;

import io.TesteLucas.libraryapi2.model.Autor;
import io.TesteLucas.libraryapi2.model.GeneroLivro;
import io.TesteLucas.libraryapi2.model.Livro;
import io.TesteLucas.libraryapi2.repositories.AutorRepository;
import io.TesteLucas.libraryapi2.repositories.LivroRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

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
        livro.setDataPublicacao(LocalDate.of(1980, 1, 2));

        Autor autor = new Autor();
        autor.setName("José");
        autor.setNacionalidade("Brasileiro");
        autor.setDataNascimento(LocalDate.of(1950, 1, 31));

        livro.setAutor(autor);

        repository.save(livro);

    }

    void atualizarAutorDoLivro(){
        UUID id = UUID.fromString("3c996f33-caa6-43ea-bc71-2348e1899621");
        var livroParaAtualizar = repository.findById(id).orElse(null);

        UUID idAutor = UUID.fromString("c9b16021-fe31-41ac-8f2d-008afd24b92f");
        Autor maria = autorRepository.findById(idAutor).orElse(null);
    }

}

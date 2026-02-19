package com.exemple.libraryapi.repository;

import com.exemple.libraryapi.model.Autor;
import com.exemple.libraryapi.model.GeneroLivro;
import com.exemple.libraryapi.model.Livro;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@SpringBootTest
class AutorRepositoryTest {


    @Autowired
    AutorRepository repository;

    @Autowired
    LivroRepository livroRepository;

    @Test
    public void salvarTest(){
        Autor autor = new Autor();
        autor.setNome("Maria");
        autor.setNacionalidade("Brasileira");
        autor.setDataNascimento(LocalDate.of(1951, 1, 31));

        var autorSalvo = repository.save(autor);
        System.out.println("Autor Salvo: " + autorSalvo);


    }

    @Test
    public void atualizarTest() {
        var id = UUID.fromString("0d3dbd7c-d544-4a5e-9d78-13fc986c6bb6");

        Optional<Autor> possivelAutor = repository.findById(id);

        if (possivelAutor.isPresent()) {

            Autor autorEncontrado = possivelAutor.get();
            System.out.println("Dados do Autor: ");
            System.out.println(possivelAutor.get());

            autorEncontrado.setDataNascimento(LocalDate.of(1960, 1,30));

            repository.save(autorEncontrado);
        }
    }

    @Test
    public void listarTest(){
        List<Autor> lista = repository.findAll();
        lista.forEach(System.out::println);
    }

    @Test
    public void countTest(){
        System.out.println("Contagem de autores: " + repository.count());
    }

    @Test
    public void deletePorIdTest(){
        var id = UUID.fromString ("669b3dee-f321-423f-8ada-9d95015d379d");
        repository.deleteById(id);
    }

    @Test
    public void deleteTest() {
        var id = UUID.fromString("d20e7020-7d29-441e-a226-5737375e8844");
        var maria = repository.findById(id).get();
        repository.deleteById(id);
        repository.delete(maria);
    }

    @Test
    void salvarAutorComLivrosTest(){
        Autor autor = new Autor();
        autor.setNome("Antonio");
        autor.setNacionalidade("Americana");
        autor.setDataNascimento (LocalDate.of(1970, 8, 5));


        Livro livro= new Livro();
        livro.setIsbn("20847-84874");
        livro.setPreco(BigDecimal.valueOf(284));
        livro.setGenero (GeneroLivro.MISTERIO);
        livro.setTitulo("0 roubo da casa assombrada");
        livro.setDataPublicacao (LocalDate.of(1999, 1, 2));
        livro.setAutor(autor);

        Livro livro2 = new Livro();
        livro2.setIsbn("99999-84874");
        livro2.setPreco(BigDecimal.valueOf(650));
        livro2.setGenero (GeneroLivro.MISTERIO);
        livro2.setTitulo("0 roubo da casa assombrada");
        livro2.setDataPublicacao (LocalDate.of(2000, 1, 2));
        livro2.setAutor(autor);

        autor.setLivros(new ArrayList<>());
        autor.getLivros().add(livro);
        autor.getLivros().add(livro2);

        repository.save(autor);

        //livroRepository.saveAll(autor.getLivros());
    }

    @Test
    void listarLivrosAutor() {
        var id = UUID.fromString("4718b068-5055-4469-9f9d-c252d14e4f20");
        var autor = repository.findById(id).get();

        List<Livro> LivrosLista = livroRepository.findByAutor(autor);
        autor.setLivros (LivrosLista);

        autor.getLivros().forEach(System.out::println);
    }

}

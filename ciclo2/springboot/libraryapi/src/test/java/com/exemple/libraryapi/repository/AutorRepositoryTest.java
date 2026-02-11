package com.exemple.libraryapi.repository;

import com.exemple.libraryapi.model.Autor;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@SpringBootTest
class AutorRepositoryTest {


    @Autowired
    AutorRepository repository;

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

}

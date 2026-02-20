package com.example.librayapi.repository;

import com.example.librayapi.model.Autor;
import com.example.librayapi.model.GeneroLivro;
import com.example.librayapi.model.Livro;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@SpringBootTest
public class AutorRepositoryTest {

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
        System.out.println("Autor salvo: " + autorSalvo);
    }

    @Test
    public void atualizarTest(){
       var id = UUID.fromString("cda9c4ec-f084-455c-bf41-007dc6b331c8");
       Optional<Autor> possivelAutor = repository.findById(id);

       if (possivelAutor.isPresent()){
           Autor autorEncontrado = possivelAutor.get();
           System.out.println("Dados do Autor: ");
           System.out.println(autorEncontrado);

           autorEncontrado.setDataNascimento(LocalDate.of(1960, 1, 30));

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
        var id = UUID.fromString("56d8426c-dd76-4e99-bf82-844754349e33");

        repository.deleteById(id);
    }


    @Test
    public void deletTest(){
        var id = UUID.fromString("a023b429-92cb-4205-8206-a2b533122af1");
        var maria = repository.findById(id).get();
        repository.delete(maria);
    }

    @Test
    void salvarAutorComLivrosTest(){
        Autor autor = new Autor();
        autor.setNome("Antonio");
        autor.setNacionalidade("Americana");
        autor.setDataNascimento(LocalDate.of(1970, 2,  13));

        Livro livro = new Livro();
        livro.setIsbn("93989-84874");
        livro.setPreco(BigDecimal.valueOf(240));
        livro.setGenero(GeneroLivro.FICCAO);
        livro.setTitulo("O roubo da casa assombrada");
        livro.setDataPublicacao(LocalDate.of(1980, 1,2));
        livro.setAutor(autor);

        Livro livro2 = new Livro();
        livro2.setIsbn("90099-84874");
        livro2.setPreco(BigDecimal.valueOf(240));
        livro2.setGenero(GeneroLivro.FICCAO);
        livro2.setTitulo("Acotar");
        livro2.setDataPublicacao(LocalDate.of(1990, 11,22));
        livro2.setAutor(autor);


        autor.setLivros(new ArrayList<>());
        autor.getLivros().add(livro);
        autor.getLivros().add(livro2);

        repository.save(autor);
        livroRepository.saveAll(autor.getLivros());
    }
}

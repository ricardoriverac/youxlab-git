package io.TesteLucas.libraryapi2.services;

import io.TesteLucas.libraryapi2.exceptions.OperacaoNaoPermitidaException;
import io.TesteLucas.libraryapi2.model.Autor;
import io.TesteLucas.libraryapi2.repositories.AutorRepository;
import io.TesteLucas.libraryapi2.repositories.LivroRepository;
import io.TesteLucas.libraryapi2.validator.AutorValidator;
import org.springframework.data.domain.Example;
import org.springframework.data.domain.ExampleMatcher;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class AutorService {

    private final AutorRepository repository;
    private final AutorValidator validator;
    private final LivroRepository livroRepository;
    public AutorService(AutorRepository repository,
                        AutorValidator autorValidator,
                        LivroRepository livroRepository){
        this.repository = repository;
        this.validator = autorValidator;
        this.livroRepository = livroRepository;
    }

    public Autor salvar(Autor autor){
        validator.validar(autor);
        return repository.save(autor);
    }

    public void atualizar(Autor autor){
        if(autor.getID() == null){
            throw new IllegalArgumentException("Para atualizar, insira um autor existente");
        }
        repository.save(autor);
    }

    public Optional<Autor> obterPorId(UUID id){
        return repository.findById(id);
    }

    public void deletar(Autor autor){
        if (possuiLivro(autor)){
            throw new OperacaoNaoPermitidaException("Não é permitido excluir um Autor que possui livros cadastrados");
        }
        repository.delete(autor);
    }

    public List<Autor> pesquisa(String nome, String nacionalidade){
        if(nome != null && nacionalidade != null){
            return repository.findByNameAndNacionalidade(nome, nacionalidade);
        }
        if (nome != null) {
            return repository.findByName(nome);
        }
        if (nacionalidade != null){
            return repository.findByNacionalidade(nacionalidade);
        }
        return repository.findAll();
    }

    public boolean possuiLivro(Autor autor){
        return livroRepository.existsByAutor(autor);
    }
    public List<Autor> pesquisaByExample(String nome, String nacionalidade){
        var autor = new Autor();
        autor.setName(nome);
        autor.setNacionalidade(nacionalidade);

        ExampleMatcher matcher = ExampleMatcher
                .matching()
                .withIgnoreNullValues()
                .withIgnoreCase()
                .withStringMatcher(ExampleMatcher.StringMatcher.CONTAINING);
        Example<Autor> autorExample = Example.of(autor, matcher);
        return repository.findAll(autorExample);
    }
}

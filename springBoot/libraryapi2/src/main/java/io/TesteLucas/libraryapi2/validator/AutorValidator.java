package io.TesteLucas.libraryapi2.validator;

import io.TesteLucas.libraryapi2.exceptions.RegistroDuplicadoException;
import io.TesteLucas.libraryapi2.model.Autor;
import io.TesteLucas.libraryapi2.repositories.AutorRepository;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
public class AutorValidator {

    private AutorRepository repository;

    public AutorValidator(AutorRepository repository) {
        this.repository = repository;
    }

    public void validar(Autor autor){
        if (existeAutorCadastrado(autor)){
            throw new RegistroDuplicadoException("Autor já cadastrado!");
        }
    }

    private boolean existeAutorCadastrado(Autor autor){
        Optional<Autor> autorEncontrado = repository.findByNameAndDataNascimentoAndNacionalidade(
                autor.getName(), autor.getDataNascimento(), autor.getNacionalidade()
        );
        if (autor.getID() == null){
            return autorEncontrado.isPresent();
        }

        return !autor.getID().equals(autorEncontrado.get().getID()) &&  autorEncontrado.isPresent();
    }
}

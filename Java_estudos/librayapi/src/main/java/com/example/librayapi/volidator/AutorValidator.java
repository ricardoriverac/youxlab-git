package com.example.librayapi.volidator;


import com.example.librayapi.excepitions.RegistroDuplicadoException;
import com.example.librayapi.model.Autor;
import com.example.librayapi.repository.AutorRepository;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
public class AutorValidator {

    private AutorRepository repository;

    public AutorValidator(AutorRepository repository) {
        this.repository = repository;
    }

    public void validar(Autor autor){
        if (exiseAutorCadastrado(autor)){
            throw  new RegistroDuplicadoException("Autor já cadastrado! ");
        }

    }

    public boolean exiseAutorCadastrado(Autor autor){
        Optional<Autor> autorEncontrado = repository.findByNomeAndDataNascimentoAndNacionalidade(
                autor.getNome(), autor.getDataNascimento(), autor.getNacionalidade()
        );

        if (autor.getId() == null){
            return autorEncontrado.isPresent();
        }

        return !autor.getId().equals(autorEncontrado.get().getId()) && autorEncontrado.isPresent();

    }
}

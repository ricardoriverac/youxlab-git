package com.example.casaDeApostas.service;

import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PutMapping;

@Service
@AllArgsConstructor
public class EsquecerSenhaService {

    private final UserRepository repository;

    public String resetarSenha(User usuarioNovaSenha){

        try {
            String senha = usuarioNovaSenha.getSenha();

            usuarioNovaSenha = new User(senha);

            repository.save(usuarioNovaSenha);

        }
        catch (NullPointerException e){
            throw new RuntimeException("Campo vazio.");
        }

        return "Senha Atualizada!";

    }


}

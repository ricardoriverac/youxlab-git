package com.example.casaDeApostas.service;

import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Optional;
import java.util.UUID;

@Service
@AllArgsConstructor
public class EsquecerSenhaService {

    private final UserRepository userRepository;

    public String resetarSenha(UUID idUsuario, String usuarioNovaSenha){

        Optional<User> user = userRepository.findById(idUsuario);

        user.get().setResetarSenha(usuarioNovaSenha);
        userRepository.save(user.get());
        return "Senha Atualizada.";

    }


}

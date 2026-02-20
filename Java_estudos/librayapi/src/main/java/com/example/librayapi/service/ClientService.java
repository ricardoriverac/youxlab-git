package com.example.librayapi.service;

import com.example.librayapi.model.Client;
import com.example.librayapi.repository.ClientRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ClientService {

    private final ClientRepository repository;

   // private final PasswordEncoder encoder;

    public Client salvar(Client client){
        //var senhaCriptografada = encoder.encode(client.getClienteSecret());
       // client.setClienteSecret(senhaCriptografada);
        return  repository.save(client);
    }

    private Client obterPorClientID(String clientid){
        return repository.findByClientID(clientid);
    }


}

package io.TesteLucas.libraryapi2.services;

import io.TesteLucas.libraryapi2.model.Client;
import io.TesteLucas.libraryapi2.repositories.ClientRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ClientService {

    private final ClientRepository repository;
    private final PasswordEncoder encoder;

    public Client salvar(Client client){
        var senhaCrptografada = encoder.encode(client.getClientId());
        client.setClientSecret(senhaCrptografada);
        return repository.save(client);
    }

    public Client obterPorClientID(String clientId){
        return repository.findByClientId(clientId);
    }
}

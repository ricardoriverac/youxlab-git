package com.example.libraryapi.security;

import com.example.libraryapi.service.ClientService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class CustomRegisteredClientRepository implements RegisteredClientRepository{

    private final ClientService clientService;
    private final TokenSettings tokenSettings;
    private final ClientSettings;
    @Override
    public void save(RegisteredClient registeredClient){}

    @Override
    public RegisteredClient findById(String id){
        return null;
    }

    @Override
    public RegisteredClient findByClientId(String clientId){
        var client = clientService.obterPorClientId(clientId);

        if(client == null){
            return null;
        }
        return RegisteredClient.withId(client.getId().toString()).clientId(client.getClientId()).clientSecret(client.getClientSecret()).redirectUri(client.getRedirectUri()).scope(client.getScope()).clientAuthenticationMethod(ClientAuthenticationMethod.CLIENT_SECRET_BASIC).authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS).build();
    }
}
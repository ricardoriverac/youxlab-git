package com.example.libraryapi.security;

//@Component
//@RequiredArgsConstructor
public class CustomRegisteredClientRepository { // implements RegisteredClientRepository

//    private final ClientService clientService;
//    private final TokenSettings tokenSettings;
//    private final ClientSettings clientSettings;
//
//    @Override
//    public void save(RegisteredClient registeredClient) {
//    }
//
//    @Override
//    public RegisteredClient findById(String id) {
//        return null;
//    }
//    @Override
//    public RegisteredClient findByClientId(String clientId) {
//        var client clientService.obter PorClientID (clientId);
//        if(client == null){
//            return null;
//        }
//        return RegisteredClient
//                .withId(client.getId().toString())
//                .clientId(client.getClientId())
//                .clientSecret(client.getClientSecret())
//                .redirectUri(client.getRedirectURI())
//                .scope (client.getScope())
//                .clientAuthenticationMethod (ClientAuthenticationMethod.CLIENT_SECRET_BASIC)
//                 .authorizationGrantType (AuthorizationGrantType.AUTHORIZATION_CODE)
//                 .authorizationGrantType (AuthorizationGrantType.CLIENT_CREDENTIALS)
//                 .tokenSettings(tokenSettings)
//                 .clientSettings(clientSettings)
//                 .build();
//    }
}
//package com.example.librayapi.security;
//
//import lombok.RequiredArgsConstructor;
//import org.springframework.stereotype.Component;
//
//@Component
//@RequiredArgsConstructor
//public class CustomRegisteredClienteRepository implements RegisteredClientRepository{
//    @Override
//    public void save(RegidteredClient regidteredClient){}
//
//    @Override
//    public RegfisteredClient findByID(String id){
//        return null;
//    }
//
//    @Override
//    public RegfisteredClient findByClientId(String clientId){
//        var clent = clinteservice.obterPorClienteId(clientId);
//        if (client == null){
//            return null;
//        }
//
//        return RegisteredCliente
//                .withId(client.getId().toString())
//                .clientId(lient.getClienteId)
//                .clientScret(client.getClientScret())
//                .redirectUri(client.getRedirectURI())
//                .scope(client.getscope)
//                .clientAuthentication Method (ClientAuthenticationMethod.CLIENT_SECRET_BASIC)
//                .authorizationGrantType (AuthorizationGrantType.AUTHORIZATION_CODE)
//                .authorizationGrantType (AuthorizationGrantType.CLIENT_CREDENTIALS)
//                .tokenSettings()
//                .clientSettings()
//                .build();
//    }
//}

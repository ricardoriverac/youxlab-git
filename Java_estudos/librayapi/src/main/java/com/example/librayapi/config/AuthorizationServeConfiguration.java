//package com.example.librayapi.config;
//
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//
//import java.time.Duration;
//
//@Configuration
//@EnableWebSecurity
//public class AuthorizationServerConfiguration {
//    @Bean
//
//    public TokenSettings tokenSettings(){
//        return TokenSettings.builder()
//                .accessTokenFormat(OAuth2TokenFormat.SELF_CONTAINED)
//                .accessTokenTimeToLive (Duration.of Minutes (60))
//                .build();
//    }
//    @Bean
//    public ClientSettings clientSettings(){
//        return ClientSettings.builder()
//                .requireAuthorizationConsent(false)
//                .build();
//    }
//
//   private RSAKey gerarChaveRSA() throws Exception { 1 usage
//        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance(algorithm: "RSA");
//        keyPairGenerator.initialize(keysize: 2048);
//        KeyPair keyPair keyPairGenerator.generateKeyPair();
//        RSAPublicKey chavePublica (RSAPublicKey) keyPair.getPublic();
//        RSAPrivateKey chavePrivada (RSAPrivateKey) keyPair.getPrivate();
//        return new RSAKey
//                .Builder(chavePublica)
//                .privateKey(chavePrivada)
//                .keyID(UUID.randomUUID().toString())
//                .build();
//    }
//    @Bean no usages
//    public JwtDecoder iwtDecoder(JWKSource<SecurityContexrt> jwkSource){

        // return OAuth2AuthorizationServerAutoConfiguration(jwkSource);

//}
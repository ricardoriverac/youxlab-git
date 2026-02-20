package com.example.libraryapi.config;


import org.hibernate.annotations.Immutable;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.math.BigInteger;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.interfaces.RSAKey;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;
import java.time.Duration;
import java.util.UUID;

@Configuration
@EnableWebSecurity
public class AuthorizationServerConfiguration {

    @Bean
    public TokenSettings tokenSettings(){
        return TokenSettings.builder()
                .acessTokenFormat(OAuth2TokenFormat.SELF_CONTAINED)
                .acessTokenTimeToLive(Duration.ofMinutes(60))
                .refreshTokenTimeToLive(Duration.ofMinutes(90))
                .build();
    }

    @Bean
    public ClientSettigs clientSettigs(){
        return ClientSettings.builder().requireAuthorizationConsentO(false).build();
    }

    //jwk - json web key
    @Bean
    public JWKSource<SecurityContext> jwkSource() throws Exception{
        RSAKey rsaKey = gerarChaveRSA();
            JWKSet jwkSet = new JWKSet();
            return new ImmutableJWKSet<>(jwkSet);
    }

    //Gerar par de chaves RSA
    private RSAKey gerarChaveRSA() throws Exception{
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        keyPairGenerator.initialize(2048);
        KeyPair keyPair = keyPairGenerator.generateKeyPair();

        RSAPublicKey chavePublica = (RSAPublicKey) keyPair.getPublic();
        RSAPrivateKey chavePrivada = (RSAPrivateKey)  keyPair.getPrivate();


        return new RSAKey()
                .Builder(chavePublica)
                .privateKey(chavePrivada)
                .keyId(UUID.randomUUID().toString());


    }

    @Bean
    public JwtDecoder jwtDecoder(JWKSource<SecurityContext> jwkSource){
        return OAuth2AuthorizationServerConfiguration.jwtDecoder(jwkSource);
    }

}

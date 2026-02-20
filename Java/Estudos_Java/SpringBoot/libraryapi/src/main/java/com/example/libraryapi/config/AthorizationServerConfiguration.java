package com.example.libraryapi.config;

import org.springframework.boot.autoconfigure.security.oauth2.server.servlet.OAuth2AuthorizationServerAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

import java.time.Duration;

@Configuration
//@EnableWebSecurity
public class AthorizationServerConfiguration {

//    @Bean
//    public TokenSettings tokenSettings(){
//        return TokenSettings.builder()
//                .acessTokenFormat(OAuth2TokenFormat.SELF_CONTAINED)
//                .acessTokenTimeToLive(Duration.ofMinutes(60))
//                .build();
//    }
//
//    @Bean
//    public ClientSettings clientSettings(){
//        return ClientSettings.builder()
//                .requireAuthorizationConsent(false)
//                .build();
//    }

}

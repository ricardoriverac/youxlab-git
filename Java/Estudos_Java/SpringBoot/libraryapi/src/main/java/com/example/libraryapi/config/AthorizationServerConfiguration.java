package com.example.libraryapi.config;
import org.springframework.boot.autoconfigure.security.oauth2.server.servlet.OAuth2AuthorizationServerAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.Order;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

import java.beans.Customizer;
import java.math.BigInteger;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.interfaces.RSAKey;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;
import java.time.Duration;
import java.util.Collection;
import java.util.List;
import java.util.UUID;

@Configuration
//@EnableWebSecurity
public class AthorizationServerConfiguration {

//    @Bean
//    @Order(1)
//    public SecurityFilterChain authServerSecurityFilterChain(HttpSecurity http) throws Exception{
//
//        OAuth2AuthorizationServerConfiguration.applyDefaultSecurity(http);
//
//        http.getConfigurer(OAuth2AuthorizationServerConfigurer.class)
//                .oidc(Customizer.withDefaults());
//
//        http.oath2ResourceServer(oauth2Rs -> oauth2Rs.jwt(Customizer.withDefaults()));
//
//        http.formLogin(configurer -> configurer.loginPage("/login"));
//
//        return http.build();
//    }
//
//    @Bean
//    public PassWordEncoder passWordEncoder(){
//
//        return new BCryptPassWordEncoder(10)
//    }

//    @Bean
//    public TokenSettings tokenSettings(){
//        return TokenSettings.builder()
//
//                .acessTokenFormat(OAuth2TokenFormat.SELF_CONTAINED)
//                .acessTokenTimeToLive(Duration.ofMinutes(60))
//                .refreshTokenTimeToLive(Duration.ofMinutes(90))
//                .build();
//    }
//
//    @Bean
//    public ClientSettings clientSettings(){
//        return ClientSettings.builder()
//                .requireAuthorizationConsent(false)
//                .build();
//    }


//    // JWK -> JSON Web Key
//    @Bean
//    public JWKSource<SecurityContext> jwkSource() throws Exception{
//
//        RSAKey rsaKey = gerarChaveRSA();
//        JWKSet jwkSet = new JWKSet(rsaKey);
//        return new ImmutableJWKSet<>(jwkSet);
//    }
//
//    // gerar par de chaves RSA
//    private RSAKey gerarChaveRSA() throws Exception {
//        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
//        KeyPairGenerator.initialize(2048);
//        KeyPair keyPair = KeyPairGenerator.generateKeyPair();
//
//        RSAPublicKey chavePublica = (RSAPublicKey) KeyPair.getPublic();
//        RSAPrivateKey chavePrivada = (RSAPrivateKey) keyPair.getPrivate();
//
//        return new RSAKey
//                .Builder(chavePublica)
//                .privateKey(chavePrivada)
//                .keyID(UUID.randomUUID().toString())
//                .build();
//    }
//
//    @Bean
//    public JwtDecoder jwtDecoder(JWKSource<SecurityContext> jwkSource){
//        return OAuth2AuthorizationServerConfiguration.jwtDecoder(jwkSource);
//    }

//    @Bean
//    public AuthorizationServerSettings authorizationServerSettings(){
//        return OAuth2AuthorizationServerSettings
//                .builder()
//                // obter token
//                .tokenEndpoint("/oauth2/token")
//                // consultar status do token
//                .tokenIntrospectionEndpoint("/oauth2/introspect")
//                // revogar
//                .tokenRevocationEndpoint("/oauth2/revoke")
//                // authorization endpoint
//                .authorizationEndpoint("/auth2/authorize")
//                // informacoes do usuario OPEN ID CONNECT
//                .oidcUserInfoEndpoint("/oauth2/userinfo")
//                // obter a chave publica pra verificar a assinatura do token
//                .jwkSetEndpoint("/oauth2/jwks")
//                // logout
//                .oidcLogoutEndpoint("oauth2/logout")
//                .build();
//    }
//    @Bean
//    public OAuth2TokenCustomizer<JwtEncodingContext> tokenCustomizer(){
//        return context -> {
//            var principal = context.getPrincipal();
//
//            if (principal instanceof CustomAuthentication authentication){
//                OAuth2TokenType tipoToken = context.getTokenType();
//
//                if (OAuth2TokenType.ACESS_TOKEN.equals(tipoToken)){
//                    Collection<GrantedAuthority> authorities = authentication.getAuthorities();
//                    List<String> authoritiesList =
//                            authorities.stream().map(GrantedAuthority::getAuthority).toList();
//                    context
//                            .getClaims()
//                            .claim("authorities", authoritiesList)
//                            .claim("email", authentication.getUsuario().getEmail());
//
//                }
//            }
//        };
//    }

}

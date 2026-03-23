package com.example.service;

import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTCreationException;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.example.model.User;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.util.Base64;

import static java.time.LocalTime.now;
import static javax.crypto.Cipher.SECRET_KEY;

@Service
public class TokenService {

    private static final String SECRET_KEY = "minha-chave-secreta-super-segura-123456";


    public String gerarToken(User user) {
        try {
            Algorithm algorithm = Algorithm.HMAC256(SECRET_KEY);

            return JWT.create()
                    .withIssuer("casaDeAposta")
                    .withSubject(user.getEmail())
                    .withClaim("id", user.getId())
                    .withClaim("role", user.getRole().toString())
                    .withExpiresAt(gerarDataExpiracao())
                    .sign(algorithm);

        } catch (JWTCreationException exception) {
            throw new RuntimeException("Erro ao gerar token JWT", exception);
        }
    }


    public String validarToken(String token) {
        try {
            Algorithm algorithm = Algorithm.HMAC256(SECRET_KEY);

            return JWT.require(algorithm)
                    .withIssuer("casaDeAposta")
                    .build()
                    .verify(token)
                    .getSubject();

        } catch (JWTVerificationException exception) {
            return null;
        }
    }

    private Instant gerarDataExpiracao() {
        // Token expira em 2 horas
        return LocalDateTime.now().plusHours(2).toInstant(ZoneOffset.of("-03:00"));
    }





}

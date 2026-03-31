package com.example.siteprojeto.service;

import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.example.siteprojeto.model.User;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneOffset;

@Service
public class TokenService {

    @Value("${api.security.secret.token}")
    private String secret;

    public String generateToken(User user) {
        return JWT.create()
                .withIssuer("auth-api")
                .withSubject(user.getLogin())
                .withExpiresAt(generateExpiration())
                .sign(Algorithm.HMAC256(secret));
    }

    public String validateToken(String token) {
        try {
            return JWT.require(Algorithm.HMAC256(secret))
                    .withIssuer("auth-api")
                    .build()
                    .verify(token)
                    .getSubject();
        } catch (JWTVerificationException e) {
            return null;
        }
    }

    private Instant generateExpiration() {
        return LocalDateTime.now()
                .plusHours(2)
                .toInstant(ZoneOffset.of("-03:00"));
    }
}
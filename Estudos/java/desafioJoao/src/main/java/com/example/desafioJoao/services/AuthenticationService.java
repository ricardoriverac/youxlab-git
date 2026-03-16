package com.example.desafioJoao.services;

import com.example.desafioJoao.dtos.LoginDTO;
import com.example.desafioJoao.models.User;
import com.example.desafioJoao.security.TokenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Service;

@Service
public class AuthenticationService {

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private TokenService tokenService;

    public String loginUser(LoginDTO data){

        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                        data.email(),
                        data.password()
                )
        );

        User user = (User) authentication.getPrincipal();

        if(!user.isEnabled()){
            throw new RuntimeException("Confirme seu email antes de fazer login");
        }


        return tokenService.generateToken(user);
    }
}
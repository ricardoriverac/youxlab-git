package com.walter.pedidosapi.services;

import com.walter.pedidosapi.configs.TokenService;
import com.walter.pedidosapi.dtos.LoginDTO;
import com.walter.pedidosapi.models.User;
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

    public String loginUser(LoginDTO loginDTO){
        Authentication authentication = authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(loginDTO.email(), loginDTO.password()));
        User user = (User) authentication.getPrincipal();

        return tokenService.generateToken(user);
    }
}

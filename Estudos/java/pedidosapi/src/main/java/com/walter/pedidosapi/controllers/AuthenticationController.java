package com.walter.pedidosapi.controllers;

import com.walter.pedidosapi.dtos.LoginDTO;
import com.walter.pedidosapi.dtos.LoginResponseDTO;
import com.walter.pedidosapi.services.AuthenticationService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
@Tag(name = "Autenticação")
public class AuthenticationController {
    private final AuthenticationService authenticationService;

    public AuthenticationController(AuthenticationService authenticationService) {
        this.authenticationService = authenticationService;
    }

    @PostMapping("/login")
    @Operation(summary = "Login", description = "Autenticar usuário e obter token")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Login realizado com sucesso"),
            @ApiResponse(responseCode = "401", description = "Credenciais inválidas"),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor")
    })
    public ResponseEntity login (@RequestBody LoginDTO data){
        String token = authenticationService.loginUser(data);
        return ResponseEntity.ok(new LoginResponseDTO(token));
    }

}
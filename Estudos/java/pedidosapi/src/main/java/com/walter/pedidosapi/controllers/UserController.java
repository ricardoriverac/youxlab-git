package com.walter.pedidosapi.controllers;


import com.walter.pedidosapi.dtos.*;
import com.walter.pedidosapi.models.User;
import com.walter.pedidosapi.services.UserService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.info.Contact;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.hibernate.boot.model.internal.CreateKeySecondPass;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/users")
@Tag( name = "Usuario")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/register")
    @Operation(summary = "Registro", description = "Registrar novo usuário")
    @ApiResponses({
           @ApiResponse(responseCode = "201", description = "Registrado com sucesso."),
            @ApiResponse(responseCode = "409", description = "Falha no registro, e-mail já possui uma conta", content = @Content)
    })
    public ResponseEntity<RegisterResponseDTO> registerUser(@RequestBody @Valid RegisterDTO data){
        RegisterResponseDTO response = userService.registerUser(data);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }
    @PostMapping("/forgot-password")
    @Operation(summary = "Senha esquecida", description = "Recuperar senha esquecida")
    @ApiResponses({
            @ApiResponse(responseCode = "204", description = "Email enviado", content = @Content),
            @ApiResponse(responseCode = "404", description = "Usuário não encontrado", content = @Content)
    })
    public ResponseEntity<Void> forgotPassword(@RequestBody @Valid ForgotEmailDTO email){
        userService.forgotPassword(email);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/reset-password/validate")
    @Operation(summary = "Resetar senha", description = "Confirmar token para resetar")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Token válido"),
            @ApiResponse(responseCode = "401", description = "Token inválido", content = @Content),
            @ApiResponse(responseCode = "410", description = "Token Expirado", content = @Content)
    })
    public String validateToken(@RequestParam String token) {
        userService.validateToken(token);
        return "Token válido";
    }

    @GetMapping()
    @Operation(summary = "Buscar todos", description = "Buscar todos os usuários")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Usuários buscados"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<PageResponseDTO<UserResponseDTO>> getAll(@RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "20") int size){
        return ResponseEntity.ok(userService.getAll(page, size));
    }

    @GetMapping("/{id}")
    @Operation(summary = "Buscar por id", description = "Buscar um usuário por id")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Usuário encontrado"),
            @ApiResponse(responseCode = "404", description = "Usuário não encontrado", content = @Content),
            @ApiResponse(responseCode = "403", description = "Não Permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<UserResponseDTO> getById(@PathVariable UUID id){
        return ResponseEntity.ok(userService.getById(id));
    }

    @GetMapping("/me")
    @Operation(summary = "Buscar meus dados", description = "Buscar os dados de minha conta")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Dados retornados"),
            @ApiResponse(responseCode = "404", description = "Usuário não encontrado", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor")
    })
    public ResponseEntity<UserResponseDTO> getMe(){
        return ResponseEntity.ok(userService.getMe());
    }

    @PatchMapping("/{id}")
    @Operation(summary = "Atualizar usuário", description = "Atualizar dados do usuário")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Dados atualizados"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "404", description = "Usuário não encontrado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<UserResponseDTO> updateUser(@PathVariable UUID id, @RequestBody @Valid UpdateUserDTO data){
        return ResponseEntity.ok(userService.updateUser(id, data));
    }

    @PatchMapping("/reset-password")
    @Operation(summary = "Resetar senha", description = "Alterar senha do usuário.")
    @ApiResponses({
            @ApiResponse(responseCode = "204", description = "Senha alterada com sucesso"),
            @ApiResponse(responseCode = "404", description = "Usuário não encontrado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<Void> resetPassword(@RequestBody ResetPasswordDTO data){
        userService.resetPassword(data);
        return ResponseEntity.noContent().build();
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Deletar usuario", description = "Deletar Usuário")
    @ApiResponses({
            @ApiResponse(responseCode = "204", description = "Usuário deletado com sucesso"),
            @ApiResponse(responseCode = "404", description = "Usuário não encontrado", content = @Content),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content)
    })
    public ResponseEntity<Void> deleteUser(@PathVariable UUID id){
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }

}

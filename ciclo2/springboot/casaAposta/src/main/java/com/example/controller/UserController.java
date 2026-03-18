package com.example.controller;


import com.example.dto.*;
import com.example.model.User;
import com.example.service.AuthService;
import com.example.service.EmailService;
import com.example.service.UserService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/user")
public class UserController {

        @Autowired
        private UserService userService;

        @Autowired
        private EmailService emailService;


        @PostMapping("/cadastro")
        public ResponseEntity<String> cadastrar(@RequestBody @Valid UserRequestDTO dados) {
            if (!dados.senhasConferem()) {
                return ResponseEntity.badRequest().body("As senhas não conferem");
            }

            User user = userService.criarUser(dados);
            emailService.enviarEmailConfirmacao(user);

            return ResponseEntity.ok("Usuário cadastrado com sucesso! Verifique seu email para confirmar o cadastro.");
        }

        @PutMapping("/atulizar/{id}")
        public ResponseEntity atualizar(@PathVariable Long id, @RequestBody UserUpdateDTO dados) {
            try {
                User  user =  userService.atualizarUser(id, dados);
                UserResponseDTO response = new UserResponseDTO(
                        user.getId(),
                        user.getNome(),
                        user.getEmail(),
                        user.getDataNascimento(),
                        user.getRole(),
                        user.getStatus(),
                        user.getEmailConfirmado()
                );
                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao atualizar: " + e.getMessage());
            }
        }


    }




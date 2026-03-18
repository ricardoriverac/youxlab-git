package com.example.controller;

import com.example.dto.*;
import com.example.model.User;
import com.example.service.AuthService;
import com.example.service.DashboardService;
import com.example.service.EmailService;
import com.example.service.UserService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/admin")
public class AdminController {

        @Autowired
        private UserService userService;


        @PostMapping("/criar-admin")
        public ResponseEntity criarAdmin(@RequestBody @Valid UserRequestDTO dados) {
            try {
                if (!dados.senhasConferem()) {
                    return ResponseEntity.badRequest().body("As senhas não conferem");
                }

                var user = userService.criarAdmin(dados);
                return ResponseEntity.ok("Admin criado com sucesso! Email: " + user.getEmail());
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao criar admin: " + e.getMessage());
            }
        }


        @GetMapping("/users")
        public ResponseEntity listarUsers(@RequestParam(required = false) String status) {
            try {
                List<User> users;

                if (status != null && !status.isEmpty()) {
                    users = userService.listarPorStatus(status);
                } else {
                    users = userService.listarTodos();
                }

                List<UserResponseDTO> response = users.stream()
                        .map(user -> new UserResponseDTO(
                                user.getId(),
                                user.getNome(),
                                user.getEmail(),
                                user.getDataNascimento(),
                                user.getRole(),
                                user.getStatus(),
                                user.getEmailConfirmado()
                        ))
                        .collect(Collectors.toList());

                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao listar usuários: " + e.getMessage());
            }
        }

        @PutMapping("/user/{id}/bloquear")
        public ResponseEntity bloquearUser(@PathVariable Long id) {
            try {
                userService.bloquearUser(id);

                User user = userService.buscarPorId(id);
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
                return ResponseEntity.badRequest().body("Erro ao bloquear usuário: " + e.getMessage());
            }
        }

        @PutMapping("/user/{id}/desbloquear")
        public ResponseEntity desbloquearUser(@PathVariable Long id) {
            try {
                userService.desbloquearUser(id);

                User user = userService.buscarPorId(id);
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
                return ResponseEntity.badRequest().body("Erro ao desbloquear usuário: " + e.getMessage());
            }
        }


        @GetMapping("/user/bloqueados")
        public ResponseEntity userBloqueados() {
            try {
                List<User> users = userService.listarBloqueados();

                List<UserResponseDTO> response = users.stream()
                        .map(user -> new UserResponseDTO(
                                user.getId(),
                                user.getNome(),
                                user.getEmail(),
                                user.getDataNascimento(),
                                user.getRole(),
                                user.getStatus(),
                                user.getEmailConfirmado()
                        ))
                        .collect(Collectors.toList());

                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Não há usuários bloqueados: " + e.getMessage());
            }
        }

        @GetMapping("/user/pendentes")
        public ResponseEntity userPendentes() {
            try {
                List<User> users = userService.listarPendentes();

                List<UserResponseDTO> response = users.stream()
                        .map(user -> new UserResponseDTO(
                                user.getId(),
                                user.getNome(),
                                user.getEmail(),
                                user.getDataNascimento(),
                                user.getRole(),
                                user.getStatus(),
                                user.getEmailConfirmado()
                        ))
                        .collect(Collectors.toList());

                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Não há usuários pendentes: " + e.getMessage());
            }
        }

        @GetMapping("/listar-todos")
        public ResponseEntity listarTodos() {
            try {
                List<User> users = userService.listarTodos();
                List<UserResponseDTO> response =  users.stream()
                        .map(user -> new UserResponseDTO(
                                user.getId(),
                                user.getNome(),
                                user.getEmail(),
                                user.getDataNascimento(),
                                user.getRole(),
                                user.getStatus(),
                                user.getEmailConfirmado()
                        ))
                        .collect(Collectors.toList());
                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao listar usuários: " + e.getMessage());
            }
        }


        @DeleteMapping("user/{id}/deletar")
        public ResponseEntity deletarUser(@PathVariable Long id) {
            try {
                userService.deletarUser(id);
                return ResponseEntity.ok("Usuário removido");
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao deletar: " + e.getMessage());
            }
        }
    }



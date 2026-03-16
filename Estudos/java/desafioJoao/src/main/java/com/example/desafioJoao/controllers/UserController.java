package com.example.desafioJoao.controllers;

import com.example.desafioJoao.dtos.AdminUserDashboardDTO;
import com.example.desafioJoao.dtos.RegisterDTO;
import com.example.desafioJoao.dtos.UserDashboardDTO;
import com.example.desafioJoao.models.User;
import com.example.desafioJoao.services.UserService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/users")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/register")
    public ResponseEntity register(@RequestBody @Valid RegisterDTO data){
        userService.createUser(data);
        return ResponseEntity.status(HttpStatus.CREATED).build();
    }

    @GetMapping("/verify")
    public ResponseEntity verify(@RequestParam String token){
        userService.confirmToken(token);
        return ResponseEntity.ok("Conta confirmada com sucesso");
    }


    @GetMapping("/me")
    public ResponseEntity<User> getUser(){
        User user = userService.getUser();
        return ResponseEntity.ok(user);
    }

    @GetMapping
    public ResponseEntity<List<User>> getAll(){
        List<User> users= userService.getAll();
        return ResponseEntity.ok(users);
    }

    @PatchMapping("/{id}/accountStatus")
    public ResponseEntity<String> accountStatus(@PathVariable UUID id){
        userService.accountStatus(id);

        return ResponseEntity.ok("Status alterado");
    }

    @GetMapping("admin/dashboard")
    public ResponseEntity<List<AdminUserDashboardDTO>> getAdminUserDashboard(){
        List<AdminUserDashboardDTO> dashboard = userService.getAdminUserDashboard();

        return ResponseEntity.ok(dashboard);
    }

    @GetMapping("/dashboard")
    public ResponseEntity<UserDashboardDTO> getUserDashboard(){
        UserDashboardDTO dashboard = userService.getUserDashboard();


        return ResponseEntity.ok(dashboard);
    }







}

package com.example.casaDeApostas.controller;

import ch.qos.logback.core.joran.conditional.IfAction;
import com.example.casaDeApostas.dto.UserDTO;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.service.AdminService;
import com.example.casaDeApostas.service.UserService;

import jakarta.validation.Valid;
import lombok.AllArgsConstructor;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.nio.file.AccessDeniedException;
import java.rmi.AccessException;
import java.util.List;

@RestController
@RequestMapping("/usuario")
@AllArgsConstructor
public class UserController {

    private final UserService userService;

    private final AdminService adminService;

    @PostMapping("user/register-users")
    public ResponseEntity register(@RequestBody @Valid UserDTO user){

        try {
            userService.createUsuario(user);

            return ResponseEntity.ok().body("Usuário criado com sucesso!");
        }
        catch (Exception e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body(e.getMessage());
        }
    }


    @PostMapping("admins/register-admins")
    public ResponseEntity createAdmin(@RequestBody @Valid UserDTO admin){

        try {
            userService.createUsuario(admin);

            return ResponseEntity.ok().body("Admin criado com sucesso!");
        }
        catch (Exception e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body(e.getMessage());
        }
    }

    @GetMapping("admins/all-users")
    public ResponseEntity allUsers(){

        List<User> allUsers = adminService.allUsers();

        return ResponseEntity.ok().body(allUsers);
    }

    @GetMapping("admins/cpf/{cpf}")
    public ResponseEntity mostrarUsuarioPorCf(@PathVariable @Valid Long cpf){
        User user = adminService.getByCpf(cpf);

        if(user == null){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Usuário não encontrado");
        }

        return ResponseEntity.ok().body(user);
    }

    @PutMapping("admins/all-users/bloquear")
    public ResponseEntity blouquar(@RequestBody boolean bloquear) throws Exception{

        //bloquear

        return ResponseEntity.ok().body("Usuario bloqueado.");
    }


}

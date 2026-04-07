package com.example.CasadeAposta.controller;

import com.example.CasadeAposta.dtos.AuthDTO;
import com.example.CasadeAposta.dtos.UserDTO;
import com.example.CasadeAposta.dtos.UserIdDTO;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/usuarios")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping
    @PreAuthorize("hasRole('ADMIN')")
    public List<User> listar(){
        return userService.listarUsuarios();
    }

    @PostMapping("/buscar")
    @PreAuthorize("hasRole('ADMIN')")
    public User buscar(@PathVariable UserIdDTO user){
        return userService.buscarPorId(user.id());
    }


    @PostMapping("/register")
    public UserDTO register(@RequestBody AuthDTO dto){
        return userService.registrar(dto);
    }

    @PutMapping("/atualizar")
    @PreAuthorize("hasAnyRole('ADMIN','USER')")
    public User atualizar(@RequestBody UserIdDTO userdto, User user){
        return userService.atualizar(userdto.id(), user);
    }


    @PutMapping("/bloquear")
    @PreAuthorize("hasRole('ADMIN')")
    public User bloquear(@RequestBody UserIdDTO user){
        return userService.bloquear(user.id());
    }


    @PutMapping("/ativar")
    @PreAuthorize("hasRole('ADMIN')")
    public User ativar(@RequestBody UserIdDTO user){
        return userService.ativar(user.id());
    }
}

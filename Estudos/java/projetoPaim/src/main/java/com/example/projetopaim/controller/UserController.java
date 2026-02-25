package com.example.projetopaim.controller;

import com.example.projetopaim.dtos.UserRequestDTO;
import com.example.projetopaim.entity.User;
import com.example.projetopaim.services.UserService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("user")
public class UserController {
    private final UserService service;

    public UserController(UserService service) {
        this.service = service;
    }

    @PostMapping("/register")
    public ResponseEntity createUser(@RequestBody @Valid UserRequestDTO){
        User user = new User();

    }


}

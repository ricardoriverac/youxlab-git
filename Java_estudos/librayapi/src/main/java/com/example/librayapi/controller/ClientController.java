package com.example.librayapi.controller;


import com.example.librayapi.model.Client;
import com.example.librayapi.service.ClientService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("clients")
@RequiredArgsConstructor
public class ClientController {


    private final ClientService service;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
  //  @PreAuthorize("hasRole('GERENTE')")
    public void salvar(@RequestBody Client client){
        service.salvar(client);
    }
}

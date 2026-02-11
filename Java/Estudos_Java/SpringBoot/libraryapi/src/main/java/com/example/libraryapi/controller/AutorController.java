package com.example.libraryapi.controller;

import com.example.libraryapi.controller.dto.AutorDTO;
import com.example.libraryapi.service.AutorService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.net.URI;

@RestController
@RequestMapping("autores")
public class AutorController {

    private final AutorService service;

    public AutorController(AutorService service){
        this.service = service;
    }

    @PostMapping
    //@RequestMapping(method = RequestMethod.POST)
    public ResponseEntity<Void> salvar(@RequestBody AutorDTO autor){
        var autorEntidade = autor.mapearParaAutor();
        service.salvar(autorEntidade);


        // http://localhost:8080/autores/7d9a00e9-3ac7-49be-a3e4-3a15419ce8a5
        URI location = ServletUriComponentsBuilder
                .fromCurrentRequest()
                .path("/" +
                        "{id}")
                .buildAndExpand(autorEntidade.getId())
                .toUri();

        return ResponseEntity.created(location).build();
    }
}

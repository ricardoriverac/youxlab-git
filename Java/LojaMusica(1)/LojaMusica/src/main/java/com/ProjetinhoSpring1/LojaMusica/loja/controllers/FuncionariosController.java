package com.ProjetinhoSpring1.LojaMusica.loja.controllers;

import com.ProjetinhoSpring1.LojaMusica.loja.entities.FuncionariosEntity;
import com.ProjetinhoSpring1.LojaMusica.loja.repositories.FuncionariosRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

@Controller
@RequestMapping("/funcionarios")
public class FuncionariosController {

    private FuncionariosRepository funcionariosRepository;

    public FuncionariosController(FuncionariosRepository funcionariosRepository){
        this.funcionariosRepository = funcionariosRepository;
    }

    @PostMapping
    private Funcionarios

}

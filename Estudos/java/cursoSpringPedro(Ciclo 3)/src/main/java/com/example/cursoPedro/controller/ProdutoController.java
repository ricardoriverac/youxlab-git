package com.example.cursoPedro.controller;

import com.example.cursoPedro.model.Produto;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("produtos")
public class ProdutoController {

    @PostMapping
    public void salvarProduto(@RequestBody Produto produto){
        System.out.println("Produto recebido: " + produto);
    }

}

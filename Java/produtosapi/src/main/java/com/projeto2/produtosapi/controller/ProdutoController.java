package com.projeto2.produtosapi.controller;

import com.projeto2.produtosapi.model.Produto;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
//mapeamento de requisições
@RequestMapping("produtos")
public class ProdutoController {
    //recebe o método
    @PostMapping
    public void salvar(Produto produto){
        System.out.println("Produto recebido: "+ produto);
    }
}

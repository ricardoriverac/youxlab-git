package com.projeto2.produtosapi.controller;

import com.projeto2.produtosapi.model.Produto;
import com.projeto2.produtosapi.repositories.ProdutoRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
//mapeamento de requisições
@RequestMapping("produtos")
public class ProdutoController {

    private ProdutoRepository produtoRepository;


    public ProdutoController(ProdutoRepository produtoRepository){
        this.produtoRepository = produtoRepository;
    }



    //recebe o método
    @PostMapping
    public Produto salvar(@RequestBody Produto produto){
        System.out.println("Produto recebido: " + produto);

        var id = UUID.randomUUID().toString();
        produto.setId(id);
        produtoRepository.save(produto);

        return produto;
    }
    @GetMapping("/{id}")
    public Produto obterPorId(@PathVariable String id){
        /*Optional<Produto> produto = produtoRepository.findById(id);
        return produto.isPresent() ? produto.get() : null;*/

        return produtoRepository.findById(id).orElse(null);
    }

    @DeleteMapping("/{id}")
    public void deletar(@PathVariable("id") String id){
        produtoRepository.deleteById(id);
    }

    @PutMapping("/{id}")
    public void atualizar(@PathVariable("id") String id, @RequestBody Produto produto){

        produto.setId(id);
        produtoRepository.save(produto);
    }

    @GetMapping
    public List<Produto> buscat(@RequestParam("nome") String nome){
        return produtoRepository.findByNome(nome);
    }



}

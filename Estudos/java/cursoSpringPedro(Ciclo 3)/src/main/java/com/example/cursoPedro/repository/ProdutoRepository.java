package com.example.cursoPedro.repository;

import com.example.cursoPedro.model.Produto;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProdutoRepository extends JpaRepository <Produto, String>{

}

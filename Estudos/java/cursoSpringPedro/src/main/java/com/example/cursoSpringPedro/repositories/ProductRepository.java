package com.example.cursoSpringPedro.repositories;

import com.example.cursoSpringPedro.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long>{

}

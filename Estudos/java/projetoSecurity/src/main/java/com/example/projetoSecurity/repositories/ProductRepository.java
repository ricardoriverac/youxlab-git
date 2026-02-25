package com.example.projetoSecurity.repositories;

import com.example.projetoSecurity.models.product.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, String> {
}
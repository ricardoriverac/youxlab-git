package com.example.Securitypro.repositores;

import com.example.Securitypro.domain.product.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, String> {
}
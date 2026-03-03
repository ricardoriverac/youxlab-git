package com.example.securityJava25.repositories;

import com.example.securityJava25.domain.product.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, String> {
}

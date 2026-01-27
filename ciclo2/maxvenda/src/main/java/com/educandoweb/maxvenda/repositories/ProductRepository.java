package com.educandoweb.maxvenda.repositories;

import com.educandoweb.maxvenda.entities.Category;
import com.educandoweb.maxvenda.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {
}

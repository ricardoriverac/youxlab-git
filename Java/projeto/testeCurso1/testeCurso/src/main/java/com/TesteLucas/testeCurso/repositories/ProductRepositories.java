package com.TesteLucas.testeCurso.repositories;

import com.TesteLucas.testeCurso.entities.Category;
import com.TesteLucas.testeCurso.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepositories extends JpaRepository<Product, Long> {
        }

package com.example.course.repositories;

import com.example.course.entities.Product;
import com.example.course.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {
}

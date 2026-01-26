package com.example.cursoSpringPedro.repositories;

import com.example.cursoSpringPedro.entities.Category;
import com.example.cursoSpringPedro.entities.Users;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CategoryRepository extends JpaRepository<Category, Long>{

}

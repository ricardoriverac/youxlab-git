package com.TesteLucas.testeCurso.repositories;

import com.TesteLucas.testeCurso.entities.Category;

import org.springframework.data.jpa.repository.JpaRepository;

public interface CategoryRepositories extends JpaRepository<Category, Long> {
        }

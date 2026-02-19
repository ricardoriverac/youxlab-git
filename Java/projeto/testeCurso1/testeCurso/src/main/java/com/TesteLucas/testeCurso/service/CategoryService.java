package com.TesteLucas.testeCurso.service;

import com.TesteLucas.testeCurso.entities.Category;
import com.TesteLucas.testeCurso.repositories.CategoryRepositories;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class CategoryService {

    @Autowired
    private CategoryRepositories repositories;

    public List<Category> findAll(){
        return repositories.findAll();
    }
    public Category findById(Long id) {
        Optional<Category> obj = repositories.findById(id);
        return obj.get();
    }

}

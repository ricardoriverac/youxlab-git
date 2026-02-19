package com.TesteLucas.testeCurso.service;

import com.TesteLucas.testeCurso.entities.Category;
import com.TesteLucas.testeCurso.entities.Product;
import com.TesteLucas.testeCurso.repositories.CategoryRepositories;
import com.TesteLucas.testeCurso.repositories.ProductRepositories;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ProductService {

    @Autowired
    private ProductRepositories repositories;

    public List<Product> findAll(){
        return repositories.findAll();
    }
    public Product findById(Long id) {
        Optional<Product> obj = repositories.findById(id);
        return obj.get();
    }

}

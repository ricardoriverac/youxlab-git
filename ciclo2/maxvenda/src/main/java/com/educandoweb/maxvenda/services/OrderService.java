package com.educandoweb.maxvenda.services;

import com.educandoweb.maxvenda.entities.Order;
import com.educandoweb.maxvenda.entities.User;
import com.educandoweb.maxvenda.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;
import java.util.Optional;

public class OrderSErvice {

    @Autowired
    private UserRepository repository;

    public List<User> findAll() {
        return repository.findAll();
    }

    public Order finById(Long id) {
        Optional<Order> obj = repository.findById(id);
        return obj.get();
    }
}

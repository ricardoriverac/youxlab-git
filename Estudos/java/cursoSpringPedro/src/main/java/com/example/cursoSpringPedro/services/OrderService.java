package com.example.cursoSpringPedro.services;

import com.example.cursoSpringPedro.entities.Order;
import com.example.cursoSpringPedro.entities.Users;
import com.example.cursoSpringPedro.repositories.OrderRepository;
import com.example.cursoSpringPedro.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class OrderService {

    @Autowired
    private OrderRepository repository;

    public List<Order> findAll(){
        return repository.findAll();
    }

    public Order findById(Long id){
        Optional<Order> obj = repository.findById(id);
        return obj.get();
    }
}

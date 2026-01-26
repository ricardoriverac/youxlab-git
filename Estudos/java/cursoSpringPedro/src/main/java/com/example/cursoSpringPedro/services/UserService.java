package com.example.cursoSpringPedro.services;

import com.example.cursoSpringPedro.entities.Users;
import com.example.cursoSpringPedro.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepository repository;

    public List<Users> findAll() {
        return repository.findAll();
    }

    public Users findById(Long id){
        Optional<Users> obj = repository.findById(id);
        return obj.get();
    }
}

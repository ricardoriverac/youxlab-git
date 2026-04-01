package com.casaaposta.service;

import com.casaaposta.model.User;
import com.casaaposta.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {

    private final UserRepository repository;

    public UserService(UserRepository repository){
        this.repository = repository;
    }

    public User create(User user){
        return repository.save(user);
    }

    public List<User> list(){
        return repository.findAll();
    }
}

package com.TesteLucas.testeCurso.service;

import com.TesteLucas.testeCurso.entities.User;
import com.TesteLucas.testeCurso.repositories.UserRepositories;
import jakarta.persistence.Entity;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepositories repositories;

    public List<User> findAll(){
        return repositories.findAll();
    }
    public User findById(Long id) {
        Optional<User> obj = repositories.findById(id);
        return obj.get();
    }

    public User insert(User obj){
        return repositories.save(obj);
    }

    public void delete(Long id){
        repositories.deleteById(id);
    }

    public User update(Long id, User obj) {
        User entity = repositories.getReferenceById(id);
        updateData(entity, obj);
        return repositories.save(entity);
    }

    private void updateData(User entity, User obj) {
        entity.setName(obj.getName());
        entity.setEmail(obj.getEmail());
        entity.setPassword(obj.getPassword());
    }
}

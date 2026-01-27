package com.example.cursoSpringPedro.services;

import com.example.cursoSpringPedro.entities.Users;
import com.example.cursoSpringPedro.repositories.UserRepository;
import com.example.cursoSpringPedro.services.exceptions.ResourceNotFoundException;
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
        return obj.orElseThrow(() -> new ResourceNotFoundException(id));
    }

    public Users insert(Users obj){
        return repository.save(obj);
    }

    public void delete(Long id){
        repository.deleteById(id);
    }

    public Users update(Long id, Users obj){
        Users entity = repository.getReferenceById(id);
        updateData(entity, obj);
        return repository.save(entity);
    }

    private void updateData (Users entity, Users obj){
        entity.setName(obj.getName());
        entity.setEmail(obj.getEmail());
        entity.setPhone(obj.getPhone());
    }
}

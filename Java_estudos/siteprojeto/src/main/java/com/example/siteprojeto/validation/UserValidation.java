package com.example.siteprojeto.validation;

import com.example.siteprojeto.repository.UserRepository;
import org.springframework.stereotype.Component;

@Component
public class UserValidation {

    private UserRepository userRepository;

    public UserValidation(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

}

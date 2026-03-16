package com.example.desafioJoao.repositories;

import com.example.desafioJoao.models.Bet;
import com.example.desafioJoao.models.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.security.core.userdetails.UserDetails;


import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface UserRepository extends JpaRepository<User, UUID> {
    UserDetails findByEmail(String email);
    boolean existsByEmail(String email);

}

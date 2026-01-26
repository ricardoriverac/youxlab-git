package com.example.cursoSpringPedro;

import com.example.cursoSpringPedro.entities.Users;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<Users, Long>{

}

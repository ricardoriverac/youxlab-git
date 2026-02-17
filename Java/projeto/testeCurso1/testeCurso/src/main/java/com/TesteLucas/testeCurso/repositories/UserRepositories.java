package com.TesteLucas.testeCurso.repositories;

import com.TesteLucas.testeCurso.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepositories extends JpaRepository<User, Long> {
}

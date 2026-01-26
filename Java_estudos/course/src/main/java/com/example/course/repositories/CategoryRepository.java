package com.example.course.repositories;

import com.example.course.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CategoryRepository extends JpaRepository<User, Long> {
}

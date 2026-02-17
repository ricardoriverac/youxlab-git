package com.TesteLucas.testeCurso.repositories;

import com.TesteLucas.testeCurso.entities.Order;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderRepositories extends JpaRepository<Order, Long> {
        }

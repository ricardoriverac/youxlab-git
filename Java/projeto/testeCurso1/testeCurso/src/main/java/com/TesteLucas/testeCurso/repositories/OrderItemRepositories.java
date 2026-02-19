package com.TesteLucas.testeCurso.repositories;


import com.TesteLucas.testeCurso.entities.OrderItem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderItemRepositories extends JpaRepository<OrderItem, Long> {
        }

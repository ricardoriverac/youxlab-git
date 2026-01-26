package com.example.cursoSpringPedro.repositories;

import com.example.cursoSpringPedro.entities.Order;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderRepository extends JpaRepository<Order, Long> {

}

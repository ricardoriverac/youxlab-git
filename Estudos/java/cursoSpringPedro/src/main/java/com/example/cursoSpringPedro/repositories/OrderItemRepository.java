package com.example.cursoSpringPedro.repositories;

import com.example.cursoSpringPedro.entities.OrderItem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderItemRepository extends JpaRepository<OrderItem, Long>{

}

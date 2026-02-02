package com.educandoweb.maxvenda.repositories;

import com.educandoweb.maxvenda.entities.OrderItem;
import com.educandoweb.maxvenda.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderItemRepository extends JpaRepository<OrderItem, Long> {
}

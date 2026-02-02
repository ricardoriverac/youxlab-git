package com.educandoweb.maxvenda.repositories;

import com.educandoweb.maxvenda.entities.Order;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderRepository extends JpaRepository<Order, Long> {
}

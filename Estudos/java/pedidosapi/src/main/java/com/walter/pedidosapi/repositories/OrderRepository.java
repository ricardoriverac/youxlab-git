package com.walter.pedidosapi.repositories;

import com.walter.pedidosapi.models.Order;
import com.walter.pedidosapi.models.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface OrderRepository extends JpaRepository<Order, UUID> {
    List<Order> findByUser(User user);
}

package com.walter.pedidosapi.services;

import com.walter.pedidosapi.dtos.*;
import com.walter.pedidosapi.models.Order;
import com.walter.pedidosapi.models.OrderItem;
import com.walter.pedidosapi.models.Product;
import com.walter.pedidosapi.models.User;
import com.walter.pedidosapi.repositories.OrderRepository;
import com.walter.pedidosapi.repositories.ProductRepository;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class OrderService {
    private final OrderRepository orderRepository;
    private final ProductRepository productRepository;

    public OrderService(OrderRepository orderRepository, ProductRepository productRepository) {
        this.orderRepository = orderRepository;
        this.productRepository = productRepository;
    }


    @Transactional
    public OrderResponseDTO createOrder(OrderRegisterDTO data) {
        User user = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        Order order = new Order();

        order.setUser(user);
        order.setOrderDate(LocalDateTime.now());
        List<OrderItem> items = new ArrayList<>();
        BigDecimal totalValue = BigDecimal.ZERO;
        for (OrderItemRegisterDTO itemsDTO : data.items()) {
            Product product = productRepository.findById(itemsDTO.productId()).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "item inexistente"));
            if (product.getStockQuantity() < itemsDTO.quantity()) {
                throw new ResponseStatusException(HttpStatus.CONFLICT, "quantidade maior que o estoque");
            }
            OrderItem item = new OrderItem();
            item.setOrder(order);
            item.setProduct(product);
            item.setQuantity(itemsDTO.quantity());
            item.setUnitPrice(product.getPrice());

            BigDecimal itemTotal = product.getPrice().multiply(BigDecimal.valueOf(itemsDTO.quantity()));
            totalValue = totalValue.add(itemTotal);

            product.setStockQuantity(product.getStockQuantity() - itemsDTO.quantity());
            items.add(item);
        }
        order.setItem(items);
        order.setTotalValue(totalValue);


        Order savedOrder = orderRepository.save(order);

        List<OrderItemResponseDTO> itemResponse = savedOrder.getItem()
                .stream()
                .map(item -> new OrderItemResponseDTO(
                        item.getId(),
                        item.getQuantity(),
                        item.getUnitPrice(),
                        item.getProduct().getId()
                ))
                .toList();

        OrderResponseDTO response = new OrderResponseDTO(savedOrder.getId(), savedOrder.getOrderDate(), savedOrder.getTotalValue(), itemResponse, savedOrder.getUser().getId());

        return response;
    }

    @Transactional(readOnly = true)
    public List<OrderResponseDTO> getAll() {
        List<Order> orders = orderRepository.findAll();
        return orders.stream().map(order -> {
            List<OrderItemResponseDTO> items = order.getItem().stream().map(item -> new OrderItemResponseDTO(item.getId(), item.getQuantity(), item.getUnitPrice(), item.getProduct().getId())).toList();
            return new OrderResponseDTO(
                    order.getId(),
                    order.getOrderDate(),
                    order.getTotalValue(),
                    items,
                    order.getUser().getId()
            );

        }).toList();
    }

    @Transactional(readOnly = true)
    public OrderResponseDTO getById(UUID id) {
        Order order = orderRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "pedido inexistente"));
        List<OrderItemResponseDTO> itemResponse = order.getItem()
                .stream()
                .map(item -> new OrderItemResponseDTO(
                        item.getId(),
                        item.getQuantity(),
                        item.getUnitPrice(),
                        item.getProduct().getId()
                ))
                .toList();
        OrderResponseDTO response = new OrderResponseDTO(order.getId(), order.getOrderDate(), order.getTotalValue(), itemResponse, order.getUser().getId());
        return response;
    }
}

//    @Transactional(readOnly = true)
//    public List<OrderResponseDTO> getOrdersMe(){
//        User auth = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
//        return orderRepository.findByUser(auth)
//                .stream()
//                .map(order ->{List<OrderItemResponseDTO> items = order.getItem().stream().map() new OrderItemResponseDTO())
//    }
//}

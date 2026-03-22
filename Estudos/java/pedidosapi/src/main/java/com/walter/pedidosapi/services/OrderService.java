package com.walter.pedidosapi.services;

import com.walter.pedidosapi.dtos.*;
import com.walter.pedidosapi.models.Order;
import com.walter.pedidosapi.models.OrderItem;
import com.walter.pedidosapi.models.Product;
import com.walter.pedidosapi.models.User;
import com.walter.pedidosapi.repositories.OrderRepository;
import com.walter.pedidosapi.repositories.ProductRepository;
import org.hibernate.type.descriptor.java.ObjectJavaType;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.HttpStatus;
import org.springframework.orm.ObjectOptimisticLockingFailureException;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.*;

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


        Order savedOrder;

        try{
            savedOrder = orderRepository.save(order);
        }catch (ObjectOptimisticLockingFailureException e){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "Estoque foi atualizado por outro pedido");
        }

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
    public PageResponseDTO<OrderResponseDTO> getAll(int page, int size) {
        size = Math.max(size, 1);
        size = Math.min(size, 50);
        Page<Order> pageResult = orderRepository.findAll(PageRequest.of(page, size));

        return new PageResponseDTO<>(
                pageResult.getContent()
                        .stream()
                        .map(o -> new OrderResponseDTO(
                                o.getId(),
                                o.getOrderDate(),
                                o.getTotalValue(),
                                o.getItem().stream()
                                                .map(i -> new OrderItemResponseDTO(
                                                        i.getId(),
                                                        i.getQuantity(),
                                                        i.getUnitPrice(),
                                                        i.getProduct().getId()
                                                ))
                                                        .toList(),
                                o.getUser().getId()
                                ))
                                .toList(),
                pageResult.getNumber(),
                pageResult.getTotalPages(),
                pageResult.getTotalElements(),
                pageResult.hasNext(),
                pageResult.hasPrevious()
        );

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


    @Transactional(readOnly = true)
    public List<OrderResponseDTO> getOrdersMe() {
        User auth = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        return orderRepository.findByUser(auth)
                .stream()
                .map(order -> new OrderResponseDTO(
                        order.getId(),
                        order.getOrderDate(),
                        order.getTotalValue(),
                        order.getItem().stream().map(item -> new OrderItemResponseDTO(item.getId(), item.getQuantity(), item.getUnitPrice(), item.getProduct().getId())).toList(), order.getUser().getId())).toList();
    }
}
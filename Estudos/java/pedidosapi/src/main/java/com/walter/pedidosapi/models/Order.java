package com.walter.pedidosapi.models;

import jakarta.persistence.*;
import lombok.*;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Entity
@Table(name = "orders")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(of = "id")
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(nullable = false, name = "id")
    private UUID id;

    @Column(nullable = false, name = "order_date")
    private LocalDateTime
            orderDate;

    @Column(nullable = false, name = "total_value", precision = 10, scale = 2)
    private BigDecimal totalValue;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL)
    private List<OrderItem> item;


    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
}

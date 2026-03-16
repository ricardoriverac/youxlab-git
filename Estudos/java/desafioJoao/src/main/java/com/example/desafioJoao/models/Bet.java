package com.example.desafioJoao.models;

import com.example.desafioJoao.enums.BetStatus;
import jakarta.persistence.*;
import lombok.*;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Entity
@Table(name = "bets")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@EqualsAndHashCode(of = "id")
public class Bet {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(nullable = false, name = "id")
    private UUID id;

    @Column(nullable = false,precision = 10, scale = 2, name = "bet_value")
    private BigDecimal betValue;

    @Column(name = "gain_value", precision = 10, scale = 2)
    private BigDecimal gainValue;

    @Column(nullable = false, name = "status")
    @Enumerated(EnumType.STRING)
    private BetStatus status;

    @Column(nullable = false, name = "number_of_diamonds")
    private int quantityDiamonds;

    @Column(nullable = false, name = "start_date")
    private LocalDateTime startDate;

    @Column(name = "end_date")
    private LocalDateTime endDate;

    @ElementCollection
    private List<Integer> bombPositions;


    @ElementCollection
    private List<Integer> revealedPositions;


    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;


}



package com.example.desafioJoao.repositories;

import com.example.desafioJoao.models.Bet;
import com.example.desafioJoao.enums.BetStatus;
import com.example.desafioJoao.models.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface BetRepository extends JpaRepository<Bet, UUID> {
    Optional<Bet> findByUserAndStatus(User user, BetStatus status);
    List<Bet> findByUser(User user);

}

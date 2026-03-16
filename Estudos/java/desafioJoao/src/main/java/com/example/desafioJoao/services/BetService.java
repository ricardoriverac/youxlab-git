package com.example.desafioJoao.services;

import com.example.desafioJoao.dtos.AdminUserDashboardDTO;
import com.example.desafioJoao.dtos.BetDTO;
import com.example.desafioJoao.dtos.BetResponseDTO;
import com.example.desafioJoao.dtos.UserDashboardDTO;
import com.example.desafioJoao.enums.BetStatus;
import com.example.desafioJoao.models.*;
import com.example.desafioJoao.repositories.BetRepository;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;


import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDateTime;
import java.util.*;

@Service
public class BetService {
    private final BetRepository repository;

    public BetService(BetRepository repository) {
        this.repository = repository;
    }

    public BetResponseDTO startBet(BetDTO data) {
        var userLogado = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        if (repository.findByUserAndStatus(userLogado, BetStatus.IN_PROGRESS).isPresent()) {
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "Não é permitido criar uma aposta com outra em andamento!"
            );
        }

        Bet newBet = new Bet();
        newBet.setUser(userLogado);
        newBet.setBetValue(data.betValue());
        newBet.setStatus(BetStatus.IN_PROGRESS);
        newBet.setGainValue(BigDecimal.ZERO);
        newBet.setQuantityDiamonds(0);
        newBet.setStartDate(LocalDateTime.now());
        newBet.setEndDate(LocalDateTime.now().plusHours(1));

        Random random = new Random();
        Set<Integer> bombs = new HashSet<>();
        while (bombs.size() < 5) {
            bombs.add(random.nextInt(25));
        }
        newBet.setBombPositions(new ArrayList<>(bombs));
        newBet.setRevealedPositions(new ArrayList<>());
        repository.save(newBet);

        return new BetResponseDTO(
                newBet.getId(),
                newBet.getStatus(),
                newBet.getBetValue(),
                newBet.getGainValue(),
                newBet.getQuantityDiamonds()
        );
    }

    public BetResponseDTO endBet() {
        User userLogado = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();

        Bet activeBet = repository.findByUserAndStatus(userLogado, BetStatus.IN_PROGRESS).orElseThrow(() -> new ResponseStatusException(
                HttpStatus.NOT_FOUND,
                "Não existe aposta ativa para este usuário"
        ));
        int diamonds = activeBet.getQuantityDiamonds();
        BigDecimal multiplier = BigDecimal.ONE.add(BigDecimal.valueOf(diamonds).multiply(new BigDecimal("0.33")));
        BigDecimal gain = activeBet.getBetValue().multiply(multiplier).setScale(2, RoundingMode.HALF_UP);
        activeBet.setGainValue(gain);
        activeBet.setStatus(BetStatus.WON);

        repository.save(activeBet);

        return new BetResponseDTO(
                activeBet.getId(),
                activeBet.getStatus(),
                activeBet.getBetValue(),
                activeBet.getGainValue(),
                activeBet.getQuantityDiamonds()
        );
    }

    public BetResponseDTO play(int position) {
        if(position > 25 || position < 0){
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Posição inválida"
            );
        }
        User userLogado = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();

        Bet activeBet = repository.findByUserAndStatus(userLogado, BetStatus.IN_PROGRESS).orElseThrow(() -> new ResponseStatusException(
                HttpStatus.NOT_FOUND,
                "Não tem apostas em andamento!"
        ));
        if (activeBet.getRevealedPositions().contains(position)) {
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "Posição já revelada!"
            );
        }
        activeBet.getRevealedPositions().add(position);
        if (activeBet.getBombPositions().contains(position)) {
            activeBet.setStatus(BetStatus.LOST);
            activeBet.setGainValue(BigDecimal.ZERO);
        } else {
            int diamonds = activeBet.getQuantityDiamonds() + 1;

            activeBet.setQuantityDiamonds(diamonds);
            BigDecimal multiplier = BigDecimal.ONE.add(BigDecimal.valueOf(diamonds).multiply(new BigDecimal("0.33")));
            BigDecimal gain = activeBet.getBetValue().multiply(multiplier).setScale(2, RoundingMode.HALF_UP);
            activeBet.setGainValue(gain);
            if (diamonds == 20) {
                activeBet.setStatus(BetStatus.WON);
            }
        }
        repository.save(activeBet);

        return new BetResponseDTO(
                activeBet.getId(),
                activeBet.getStatus(),
                activeBet.getBetValue(),
                activeBet.getGainValue(),
                activeBet.getQuantityDiamonds()
        );
    }

    public BetResponseDTO getCurrent() {
        User userLogado = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();

        Bet activeBet = repository.findByUserAndStatus(userLogado, BetStatus.IN_PROGRESS).orElseThrow(() -> new RuntimeException("Não tem apostas em andamento!"));
        return new BetResponseDTO(
                activeBet.getId(),
                activeBet.getStatus(),
                activeBet.getBetValue(),
                activeBet.getGainValue(),
                activeBet.getQuantityDiamonds()
        );
    }

    public List<BetResponseDTO> getHistory() {
        User userLogado = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        List<Bet> bets = repository.findByUser(userLogado);
        return bets.stream().map(bet -> new BetResponseDTO(bet.getId(), bet.getStatus(), bet.getBetValue(), bet.getGainValue(), bet.getQuantityDiamonds())).toList();
    }
}
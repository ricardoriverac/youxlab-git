package com.example.desafioJoao.controllers;

import com.example.desafioJoao.dtos.BetDTO;
import com.example.desafioJoao.dtos.BetResponseDTO;
import com.example.desafioJoao.dtos.UserDashboardDTO;
import com.example.desafioJoao.services.BetService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/bets")
public class BetController {
    private final BetService betService;

    public BetController(BetService betService) {
        this.betService = betService;
    }

    @PostMapping("/start")
    public ResponseEntity<BetResponseDTO> startBet(@RequestBody @Valid BetDTO data){
        BetResponseDTO response = betService.startBet(data);

        return ResponseEntity.ok(response);
    }
    @PostMapping("/end")
    public ResponseEntity<BetResponseDTO> endBet(){
        BetResponseDTO response =  betService.endBet();


        return ResponseEntity.ok(response);
    }

    @PostMapping("/play")
    public ResponseEntity<BetResponseDTO> play(@RequestBody  int position){
        BetResponseDTO response = betService.play(position);

        return ResponseEntity.ok(response);
    }

    @GetMapping("/current")
    public ResponseEntity<BetResponseDTO> getCurrent(){
        BetResponseDTO response = betService.getCurrent();

        return ResponseEntity.ok(response);
    }
    @GetMapping("/history")
    public ResponseEntity<List<BetResponseDTO>> getHistory(){
        List<BetResponseDTO> response = betService.getHistory();
        return ResponseEntity.ok(response);
    }
}

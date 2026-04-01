
package com.casaaposta.controller;

import com.casaaposta.model.Game;
import com.casaaposta.service.GameService;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

@RestController
@RequestMapping("/game")
public class GameController {

 private final GameService service;

 public GameController(GameService service){
  this.service = service;
 }

 @PostMapping("/start/{userId}/{bet}")
 public Game start(@PathVariable UUID userId, @PathVariable double bet){
  return service.startGame(userId, bet);
 }

 @PostMapping("/open/{gameId}")
 public Game open(@PathVariable UUID gameId){
  return service.open(gameId);
 }

 @PostMapping("/finish/{gameId}")
 public Game finish(@PathVariable UUID gameId){
  return service.finish(gameId);
 }

}

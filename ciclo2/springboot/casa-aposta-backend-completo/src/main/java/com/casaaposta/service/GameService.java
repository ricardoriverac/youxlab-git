
package com.casaaposta.service;

import com.casaaposta.model.Game;
import com.casaaposta.repository.GameRepository;
import org.springframework.stereotype.Service;

import java.util.Random;
import java.util.UUID;

@Service
public class GameService {

 private final GameRepository repository;

 public GameService(GameRepository repository){
  this.repository = repository;
 }

 public Game startGame(UUID userId, double bet){

  Game g = new Game();
  g.setUserId(userId);
  g.setBetValue(bet);
  g.setDiamonds(0);
  g.setFinished(false);

  return repository.save(g);
 }

 public Game open(UUID gameId){

  Game g = repository.findById(gameId).orElseThrow();

  Random r = new Random();

  boolean bomb = r.nextInt(5) == 0;

  if(bomb){
   g.setFinished(true);
   g.setWinValue(0);
  } else{
   g.setDiamonds(g.getDiamonds()+1);
  }

  return repository.save(g);
 }

 public Game finish(UUID gameId){

  Game g = repository.findById(gameId).orElseThrow();

  double result = g.getBetValue() * (1 + (g.getDiamonds() * 0.33));

  g.setWinValue(result);
  g.setFinished(true);

  return repository.save(g);
 }

}

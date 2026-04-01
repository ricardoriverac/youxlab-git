
package com.casaaposta.model;

import jakarta.persistence.*;
import java.util.UUID;

@Entity
public class Game {

 @Id
 @GeneratedValue
 private UUID id;

 private UUID userId;
 private double betValue;
 private int diamonds;
 private boolean finished;
 private double winValue;

 public UUID getId(){ return id; }

 public UUID getUserId(){ return userId; }
 public void setUserId(UUID userId){ this.userId = userId; }

 public double getBetValue(){ return betValue; }
 public void setBetValue(double betValue){ this.betValue = betValue; }

 public int getDiamonds(){ return diamonds; }
 public void setDiamonds(int diamonds){ this.diamonds = diamonds; }

 public boolean isFinished(){ return finished; }
 public void setFinished(boolean finished){ this.finished = finished; }

 public double getWinValue(){ return winValue; }
 public void setWinValue(double winValue){ this.winValue = winValue; }
}


package com.casaaposta.model;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.util.UUID;

@Entity
public class User {

 @Id
 @GeneratedValue
 private UUID id;

 private String name;
 private String email;
 private String password;
 private LocalDate birthDate;
 private String role;
 private boolean blocked;

 public UUID getId(){ return id; }

 public String getName(){ return name; }
 public void setName(String name){ this.name = name; }

 public String getEmail(){ return email; }
 public void setEmail(String email){ this.email = email; }

 public String getPassword(){ return password; }
 public void setPassword(String password){ this.password = password; }

 public LocalDate getBirthDate(){ return birthDate; }
 public void setBirthDate(LocalDate birthDate){ this.birthDate = birthDate; }

 public String getRole(){ return role; }
 public void setRole(String role){ this.role = role; }

 public boolean isBlocked(){ return blocked; }
 public void setBlocked(boolean blocked){ this.blocked = blocked; }
}

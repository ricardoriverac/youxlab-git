
package com.casaaposta.service;

import com.casaaposta.model.User;
import com.casaaposta.repository.UserRepository;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {

 private final UserRepository repository;
 private final BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();

 public UserService(UserRepository repository){
  this.repository = repository;
 }

 public User register(User user){
  user.setPassword(encoder.encode(user.getPassword()));
  user.setRole("USER");
  return repository.save(user);
 }

 public List<User> list(){
  return repository.findAll();
 }

}

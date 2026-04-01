
package com.casaaposta.controller;

import com.casaaposta.model.User;
import com.casaaposta.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {

 private final UserService service;

 public UserController(UserService service){
  this.service = service;
 }

 @PostMapping
 public User register(@RequestBody User user){
  return service.register(user);
 }

 @GetMapping
 public List<User> list(){
  return service.list();
 }

}

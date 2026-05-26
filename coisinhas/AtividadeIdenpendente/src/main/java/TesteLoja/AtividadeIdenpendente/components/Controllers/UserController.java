package TesteLoja.AtividadeIdenpendente.components.Controllers;

import TesteLoja.AtividadeIdenpendente.components.Repositories.UserRepository;
import TesteLoja.AtividadeIdenpendente.components.entities.User;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RestController
@RequestMapping("/user")
public class UserController {

    private UserRepository repository;

    public UserController(UserRepository repository){
        this.repository = repository;
    }

    @GetMapping("/{id}")
    public User getando(@PathVariable Long id){
        return repository.findById(id).orElse(null);
    }

    @PostMapping
    public User postando(@RequestBody User user){
        return repository.save(user);
    }
    @PutMapping
    public void atualizando(@RequestBody User user){
        repository.save(user);
    }



}

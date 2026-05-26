package io.github.cursodsousa.arquiteturaSpring.todos;

import org.jspecify.annotations.NonNull;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("/todos")
public class TodoController {

    private TodoService service;

    public TodoController(TodoService service){
        this.service = service;
    }

    @PostMapping
    public TodoEntity salvar(@RequestBody TodoEntity todo){
        try {
            return this.service.salvar(todo);
        }catch (IllegalArgumentException illegalArgumentException){
        var mensagemErro = illegalArgumentException.getMessage();
        throw new ResponseStatusException(HttpStatus.BAD_REQUEST, mensagemErro);
        }

    }

    @PutMapping("{id}")
    public void atualizarStatus(
            @PathVariable("id") Integer id, @RequestBody @NonNull TodoEntity todo)
    {
        todo.setId(id);
        service.atualizarStatus(todo);
    }

    @GetMapping("{id}")
    public TodoEntity buscar(@PathVariable("id") Integer id){
        return service.buscarPorId(id);
    }
}

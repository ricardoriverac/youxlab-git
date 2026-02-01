package com.example.arquiteturaspring.todos;


import org.springframework.stereotype.Component;

@Component
public class TodoValidator {


    private TodoRepository todoRepository;

    public TodoValidator(TodoRepository todoRepository) {
        this.todoRepository = todoRepository;
    }

    public void validar(TodoEntity todo) throws IllegalAccessException {
        if (existeTodoComDescricao(todo.getDescricao())){
            throw new IllegalAccessException("Ja existe Todo com essa descricao! ");
        }

    }


    private boolean existeTodoComDescricao(String descricao){
        return todoRepository.existsByDescricao(descricao);

    }
}

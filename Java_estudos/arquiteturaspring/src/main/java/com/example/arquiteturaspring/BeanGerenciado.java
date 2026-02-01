package com.example.arquiteturaspring;


import com.example.arquiteturaspring.todos.TodoEntity;
import com.example.arquiteturaspring.todos.TodoValidator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.context.annotation.Lazy;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;



@Lazy
@Component
@Scope(BeanDefinition.SCOPE_SINGLETON)
public class BeanGerenciado {



    private String idUsuarioLogado;

    @Autowired
    private TodoValidator validator;


    public void utilizar() throws IllegalAccessException {
        var todo = new TodoEntity();
        validator.validar(todo);
    }


    @Autowired
    public void setValidator(TodoValidator validator){
        this.validator = validator;
    }
}

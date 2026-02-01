package com.example.arquiteturaspring.todos;

import org.springframework.stereotype.Service;

@Service
public class TodoService {




    private TodoRepository repository;
    private TodoValidator validator;
    private MailSender mailSender;


    public TodoService(TodoRepository repository, MailSender mailSender, TodoValidator validator) {
        this.repository = repository;
        this.mailSender = mailSender;
        this.validator = validator;
    }

    public TodoEntity salvar(TodoEntity novoTodo) throws IllegalAccessException {
        validator.validar(novoTodo);
        return repository.save(novoTodo);
    }


    public void atualizarStatus(TodoEntity todo){
        repository.save(todo);
        String status = todo.getConcluido() == Boolean.TRUE ? "Concluido" : "Não concluido";
        mailSender.enviar("Todo" + todo.getDescricao() + "foi atualizado para " + status);

    }

    public TodoEntity buscarPorId(Integer id){
        return repository.findById(id).orElse(null);
    }
}

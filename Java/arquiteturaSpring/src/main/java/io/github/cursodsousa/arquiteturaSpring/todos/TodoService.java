package io.github.cursodsousa.arquiteturaSpring.todos;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class TodoService  {

    private TodoRepository repository;
    private TodoValidator validator;
    private MailSender mailSender;


    public TodoService(TodoRepository todoRepository, TodoValidator validator, MailSender mailSender){
        this.repository = todoRepository;
        this.validator = validator;
        this.mailSender = mailSender;
    }

    public TodoEntity salvar(TodoEntity novoTodo){
        validator.validar(novoTodo);
        return repository.save(novoTodo);
    }
    public void atualizarStatus(TodoEntity todo){
        repository.save(todo);
        String concluido = todo.getConcluido() == Boolean.TRUE ? "Concluído" : "Não concluído";
        mailSender.enviar("Todo: " + todo.getDescricao() + "foi " + concluido);
    }

    public TodoEntity buscarPorId(Integer id){
        return repository.findById(id).orElse(null);

    }
}

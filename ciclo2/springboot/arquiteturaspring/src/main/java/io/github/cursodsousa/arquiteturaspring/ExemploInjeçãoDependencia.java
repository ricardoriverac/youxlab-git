package io.github.cursodsousa.arquiteturaspring;

import io.github.cursodsousa.arquiteturaspring.Todos.*;
import jakarta.persistence.EntityManager;
import org.springframework.data.jpa.repository.support.SimpleJpaRepository;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import java.sql.Connection;

public class ExemploInjeçãoDependencia {

    public static void main(String[] args) throws Exception{

        DriverManagerDataSource dataSource =  new DriverManagerDataSource();
        dataSource.setUrl("url");
        dataSource.setUsername("user");
        dataSource.setPassword("password");

        Connection connection = dataSource.getConnection();

        EntityManager entityManager = null;

        TodoRepository repository = null; // new SimpleJpaRepository<TodoEntity, Integer>();

        TodoValidator todoValidator= new TodoValidator(repository);
        MailSender sender = new MailSender();
        TodoService todoservice = new TodoService(repository, todoValidator, sender);

//        BeanGerenciado beanGerenciado = new BeanGerenciado (null);
//        beanGerenciado.setValidator (todoValidator);
//        if(codicao == true){
//            beanGerenciado.setValidator();

    }

}

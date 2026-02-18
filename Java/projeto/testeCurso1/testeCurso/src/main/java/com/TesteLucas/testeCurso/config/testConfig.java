package com.TesteLucas.testeCurso.config;


import com.TesteLucas.testeCurso.entities.Category;
import com.TesteLucas.testeCurso.entities.Order;
import com.TesteLucas.testeCurso.entities.User;
import com.TesteLucas.testeCurso.entities.enums.OrderStatus;
import com.TesteLucas.testeCurso.repositories.CategoryRepositories;
import com.TesteLucas.testeCurso.repositories.OrderRepositories;
import com.TesteLucas.testeCurso.repositories.UserRepositories;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

import java.time.Instant;
import java.util.Arrays;

@Configuration
@Profile("test")
public class testConfig implements CommandLineRunner {

    @Autowired
    private UserRepositories userRepositories;
    @Autowired
    private OrderRepositories orderRepositories;
    @Autowired
    private CategoryRepositories categoryRepositories;

    @Override
    public void run(String... args) throws Exception {
        User u1 = new User(null, "Maria Brown", "maria1@gmail.com", "98888888", "123456");
        User u2 = new User(null, "Alex Green", "alex1@gmail.com", "9777777", "234567");
        User u3 = new User(null, "Atena", "atena123@email.com", "999999", "ksgkhsgk3");

        Order o1 = new Order(null, Instant.parse("2019-06-20T19:53:07Z"), u1, OrderStatus.PAID);
        Order o2 = new Order(null, Instant.parse("2019-07-21T03:42:10Z"), u2, OrderStatus.WAITING_PAYMENT);
        Order o3 = new Order(null, Instant.parse("2019-07-22T15:21:22Z"), u3, OrderStatus.DELIVIERED);

        Category c1 = new Category(null, "Eletronics");
        Category c2 = new Category(null, "Dishes");
        Category c3 = new Category(null, "Furniture");

        userRepositories.saveAll(Arrays.asList(u1, u2, u3));
        orderRepositories.saveAll(Arrays.asList(o1, o2, o3));
        categoryRepositories.saveAll(Arrays.asList(c1, c2, c3));
    }
}

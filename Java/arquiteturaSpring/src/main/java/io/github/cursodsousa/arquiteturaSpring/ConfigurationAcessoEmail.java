package io.github.cursodsousa.arquiteturaSpring;

import io.github.cursodsousa.arquiteturaSpring.todos.MailSender;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ConfigurationAcessoEmail {

    @Autowired
    private AppProperties properties;


    private MailSender mailSender(){
        return null;
    };
}

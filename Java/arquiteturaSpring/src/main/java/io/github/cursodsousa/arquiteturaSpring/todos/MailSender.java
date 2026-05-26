package io.github.cursodsousa.arquiteturaSpring.todos;

import org.springframework.stereotype.Component;

@Component
public class MailSender {

    public void enviar(String mensagem){
        System.out.println("enviando email: " + mensagem);
    }
}

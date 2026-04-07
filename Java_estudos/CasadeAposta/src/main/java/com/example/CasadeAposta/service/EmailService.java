package com.example.CasadeAposta.service;

import lombok.RequiredArgsConstructor;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class EmailService {

    private final JavaMailSender mailSender;

    public void enviarEmail(String para, String assunto, String texto){

        SimpleMailMessage message = new SimpleMailMessage();

        message.setTo(para);
        message.setSubject(assunto);
        message.setText(texto);

        mailSender.send(message);
    }
}
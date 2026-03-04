package com.example.service;

import org.springframework.stereotype.Service;

@Service
public class EmailService {

    @Autowired
    private JavaMailSender mailSender;

    public void enviarEmailConfirmacao(String destinatario, String token) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(destinatario);
        message.setSubject("Confirme seu cadastro - Casa de Aposta");
        message.setText("Olá!\n\n" +
                "Para confirmar seu cadastro, clique no link:\n" +
                "http://localhost:8080/auth/confirmar-email?token=" + token + "\n\n" +
                "Link válido por 24 horas.\n\n" +
                "Casa de Aposta");

        mailSender.send(message);
        System.out.println("Email enviado para: " + destinatario);
    }

    public void enviarEmailRecuperacao(String destinatario, String token) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(destinatario);
        message.setSubject("Recuperação de senha - Casa de Aposta");
        message.setText("Olá!\n\n" +
                "Para redefinir sua senha, clique no link:\n" +
                "http://localhost:8080/auth/redefinir-senha?token=" + token + "\n\n" +
                "Link válido por 1 hora.\n\n" +
                "Casa de Aposta");

        mailSender.send(message);
        System.out.println("Email de recuperação enviado para: " + destinatario);
    }
}

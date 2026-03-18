package com.example.service;

import com.example.model.User;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

    public void enviarEmailConfirmacao(User user) {
        System.out.println("Email de confirmação");
        System.out.println("Para: " + user.getEmail());
        System.out.println("Link: http://localhost:3000/confirmar-email?token=" + user.getTokenConfirmacao());
    }

    public void enviarEmailResetSenha(String destinatario, String token) {
        System.out.println(" Email de reset de senha ");
        System.out.println("Para: " + destinatario);
        System.out.println("Link: http://localhost:3000/resetar-senha?token=" + token);
    }

    }


package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.AccountDTO;
import com.example.casaDeApostas.model.conta.Account;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.AccountRepository;
import com.example.casaDeApostas.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;


@Service
@AllArgsConstructor
public class AccountService {

    private final AccountRepository accountRepository;

    private final UserRepository userRepository;


    public String createAccount(AccountDTO conta){

        try {
            Account newAccount = new Account(
                    conta.cpf(),
                    conta.valorAtual()
            );

            User user = userRepository.findByCpf(newAccount.getCpf());
            boolean cpf = accountRepository.existsByCpf(user.getCpf());
            boolean existeEsseCpf = userRepository.existsByCpf(newAccount.getCpf());

            if (!existeEsseCpf){
                return "Erro: Esse CPF não existe.";
            }

            if (cpf) {
                return "Erro: CPF já cadastrado.";
            }

            accountRepository.save(newAccount);
            return "Conta criada com sucesso!";

        } catch (NullPointerException exception) {
            throw new RuntimeException("Conta não preenchida corretamente.");
        }
    }
}

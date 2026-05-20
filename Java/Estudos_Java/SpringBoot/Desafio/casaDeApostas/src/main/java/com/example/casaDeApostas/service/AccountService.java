package com.example.casaDeApostas.service;

import com.example.casaDeApostas.dto.AccountDTO;
import com.example.casaDeApostas.exceptions.CpfJaCadastrado;
import com.example.casaDeApostas.exceptions.NaoPodeDepositarValorNegativo;
import com.example.casaDeApostas.model.conta.Account;
import com.example.casaDeApostas.model.users.User;
import com.example.casaDeApostas.repository.AccountRepository;
import com.example.casaDeApostas.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;


@Service
@AllArgsConstructor
public class AccountService {

    private final AccountRepository accountRepository;

    private final UserRepository userRepository;


    public String createAccount(AccountDTO conta) {
        Account newAccount = new Account(
                conta.cpf(),
                conta.valorAtual()
        );

        User user = userRepository.findByCpf(conta.cpf());

        if (user ==  null) {
            throw new IllegalArgumentException("Cpf não válido.");
        }

        boolean existeEsseCpf = accountRepository.existsByCpf(newAccount.getCpf());

        if (existeEsseCpf) {
            throw new CpfJaCadastrado("Erro: CPF já cadastrado.");
        }

        accountRepository.save(newAccount);
        return "Conta criada com sucesso!";
    }

    public void depositar(Long cpf, Double valor){

        Account account = accountRepository.findByCpf(cpf);
        if (account == null)
            throw new IllegalArgumentException("Cpf não existe.");

        if (valor < 0){
            throw new NaoPodeDepositarValorNegativo("Não pode depositar valor negativo.");
        }
        account.depositar(valor);
        accountRepository.save(account);
    }

}

package com.example.casaDeApostas.controller;

import com.example.casaDeApostas.dto.AccountDTO;
import com.example.casaDeApostas.dto.DepositoDTO;
import com.example.casaDeApostas.model.conta.Account;
import com.example.casaDeApostas.service.AccountService;
import jakarta.validation.Valid;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/account")
@AllArgsConstructor
public class AccountController {

    private final AccountService accountService;

    @PostMapping("/create-account")
    public ResponseEntity createAccount(@RequestBody @Valid AccountDTO conta)  {

        String account = accountService.createAccount(conta);

        return ResponseEntity.ok().body(account);
    }

    @PostMapping("/depositar")
    public ResponseEntity deposito(
            @RequestBody DepositoDTO dto){
        accountService.depositar(dto.cpf(), dto.valor());

        return ResponseEntity.ok().body("Deposito feito!");
    }



}

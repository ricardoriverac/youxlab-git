package com.example.casaDeApostas.controller;

import com.example.casaDeApostas.dto.AccountDTO;
import com.example.casaDeApostas.dto.DepositoDTO;
import com.example.casaDeApostas.exceptions.CpfJaCadastrado;
import com.example.casaDeApostas.exceptions.NaoPodeDepositarValorNegativo;
import com.example.casaDeApostas.service.AccountService;
import jakarta.validation.Valid;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/account")
@AllArgsConstructor
public class AccountController {

    private final AccountService accountService;

    @PostMapping("/create-account")
    public ResponseEntity createAccount(@RequestBody @Valid AccountDTO conta)  {

        try {
            String account = accountService.createAccount(conta);

            return ResponseEntity.ok().body(account);
        }
        catch (CpfJaCadastrado c){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Cpf já cadastrado.");
        }
        catch (IllegalArgumentException e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Cpf inválido.");
        }
    }

    @PostMapping("/depositar")
    public ResponseEntity deposito(
            @RequestBody DepositoDTO dto){

        try {
            accountService.depositar(dto.cpf(), dto.valor());
            return ResponseEntity.ok().body("Deposito feito!");
        }
        catch (NaoPodeDepositarValorNegativo e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Não pode depositar valor negativo.");
        }
        catch (IllegalArgumentException e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body("Cpf inválido.");
        }
    }

}

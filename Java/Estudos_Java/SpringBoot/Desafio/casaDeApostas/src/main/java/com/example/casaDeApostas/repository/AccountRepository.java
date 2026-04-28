package com.example.casaDeApostas.repository;

import com.example.casaDeApostas.model.conta.Account;
import com.example.casaDeApostas.model.users.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface AccountRepository extends JpaRepository<Account, UUID> {

    boolean existsByCpf(Long cpf);

    Account findByCpf(Long cpf);

}

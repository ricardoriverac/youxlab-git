package com.example.libraryapi.repository;

import com.example.libraryapi.model.Client;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;


public class ClientRepository extends JpaRepository<Client, UUID> {
    public Client findByClientId(String clientId) {
    }

    X
}

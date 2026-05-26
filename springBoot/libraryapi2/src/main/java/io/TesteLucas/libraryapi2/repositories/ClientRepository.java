package io.TesteLucas.libraryapi2.repositories;

import io.TesteLucas.libraryapi2.model.Client;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface ClientRepository extends JpaRepository<Client, UUID> {
    Client findByClientId(String clientId);
}

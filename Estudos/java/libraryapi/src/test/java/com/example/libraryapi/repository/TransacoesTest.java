package com.example.libraryapi.repository;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;

public class TransacoesTest {
    @Autowired
    AutorRepository autorRepository;

    @Test
    @Transactional
    void transacaoSimples(){

    }
}

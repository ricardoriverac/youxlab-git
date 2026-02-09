package com.example.librayapi.service;

import com.example.librayapi.repository.AutorRepository;
import com.example.librayapi.repository.LivroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;


@Service
public class TransacaoService {

    @Autowired
    private AutorRepository autorRepository;
    @Autowired
    private LivroRepository livroRepository;


    @Transactional
    public void executar(){

    }
}

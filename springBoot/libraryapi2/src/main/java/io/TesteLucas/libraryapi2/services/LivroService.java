package io.TesteLucas.libraryapi2.services;

import io.TesteLucas.libraryapi2.repositories.LivroRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class LivroService {

    private final LivroRepository repository;
}

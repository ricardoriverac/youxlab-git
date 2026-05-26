package io.TesteLucas.libraryapi2.controller;

import io.TesteLucas.libraryapi2.services.LivroService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("livro")
@RequiredArgsConstructor
public class LIvroController {

    private final LivroService service;
}

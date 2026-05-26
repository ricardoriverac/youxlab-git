package com.libraryAtividade.libraryAtividade.service;


import com.libraryAtividade.libraryAtividade.dto.BookDTO;
import com.libraryAtividade.libraryAtividade.mapper.BookMapper;
import com.libraryAtividade.libraryAtividade.model.Book;
import com.libraryAtividade.libraryAtividade.repositories.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;


@Service

public class BookService {
    @Autowired
    private BookRepository repository;

    public List<BookDTO> buscarTodos(){
        return repository.findAll()
                .stream()
                .map(BookMapper::toDto)
                .toList();
    }

    public Optional<Book> buscando (UUID id){
        return repository.findById(id);
    }

    public Optional<Book> obtendo(UUID id){

        Optional<Book> searching = buscando(id);
        if (searching.isEmpty()){
            return null;
        }
        return searching;
    }

    public Book atualizar (Book book){
        if (book.getId() == null){
            return null;
        }
        return repository.save(book);
    }

    public void deletando (UUID id){
        if (buscando(id).isEmpty()) {
            throw new RuntimeException("Nenhum livro para deletar");
        }
        Book book = buscando(id).orElse(null);
        repository.delete(book);
    }

    public Book emprestando(UUID id){
        Book book = repository.findById(id).orElseThrow(() -> new RuntimeException("Livro não encontrado"));

        if (!book.getDisponibility()){
            throw new RuntimeException("Livro já está emprestado");
        }
        book.setDisponibility(false);

        return repository.save(book);
    }

    public Book devolver(UUID id){
        Book book = repository.findById(id).orElseThrow(() -> new RuntimeException("Livro não encontrado"));

        book.setDisponibility(true);

        return repository.save(book);
    }

}

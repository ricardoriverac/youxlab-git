package com.libraryAtividade.libraryAtividade.controllers;

import com.libraryAtividade.libraryAtividade.dto.BookDTO;
import com.libraryAtividade.libraryAtividade.mapper.BookMapper;
import com.libraryAtividade.libraryAtividade.model.Book;
import com.libraryAtividade.libraryAtividade.repositories.BookRepository;
import com.libraryAtividade.libraryAtividade.service.BookService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("book")
public class BookController {

    private BookRepository repository;
    private BookService service;
    public BookController(BookRepository repository, BookService service){
        this.repository = repository;
        this.service = service;
    }
    @PostMapping
    public ResponseEntity<BookDTO> postando(@RequestBody BookDTO dto){
        Book book = BookMapper.toEntity(dto);

        Book salvo = repository.save(book);

        return ResponseEntity.ok(BookMapper.toDto(salvo));
    }

    @GetMapping
    public ResponseEntity<List<BookDTO>> listandoTodos (){
        List<BookDTO> bookDTOS = service.buscarTodos();

        return ResponseEntity.ok(bookDTOS);
    }
    @GetMapping("{id}")
    public ResponseEntity<BookDTO> buscandoPorId(@PathVariable("id") UUID id){
        /*var buscado = UUID.fromString(id);
        Optional<Book> book = service.buscando(buscado);
        if (book.isPresent()){
            BookDTO dto = BookMapper.toDto(book.get());
        }
        return ResponseEntity.notFound().build();*/
        return service.buscando(id)
                .map(BookMapper::toDto)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PutMapping("{id}")
    public ResponseEntity<Optional<BookDTO>> atualizar(@PathVariable("id") UUID id, @RequestBody BookDTO dto){

        if (service.obtendo(id).isEmpty()){

            return ResponseEntity.notFound().build();
        }
        Optional<Book> newBook =  service.obtendo(id);
        var book = newBook.get();
        book.setTitulo(dto.titulo());
        book.setAutor(dto.autor());
        book.setAnoPublicacao(dto.anoPublicacao());
        book.setIsbn(dto.isbn());
        book.setDisponibility(dto.Disponibility());
        Book savingPut = service.atualizar(book);
        return ResponseEntity.noContent().build();

    }

    public void deletando(@PathVariable UUID id){

        if (service.buscando(id).isEmpty()){
            ResponseEntity.notFound().build();
        }
        service.deletando(id);
    }



}

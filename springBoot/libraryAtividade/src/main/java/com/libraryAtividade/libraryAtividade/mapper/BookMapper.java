package com.libraryAtividade.libraryAtividade.mapper;


import com.libraryAtividade.libraryAtividade.dto.BookDTO;
import com.libraryAtividade.libraryAtividade.model.Book;

public class BookMapper {



    public static BookDTO toDto(Book book){

        return new BookDTO(book.getTitulo(), book.getAutor(), book.getAnoPublicacao(), book.getIsbn(), book.getDisponibility());

    }

    public static Book toEntity(BookDTO dto){
        Book book = new Book();
        book.setAutor(dto.autor());
        book.setTitulo(dto.titulo());
        book.setAnoPublicacao(dto.anoPublicacao());
        book.setIsbn(dto.isbn());
        book.setDisponibility(dto.Disponibility());
        return book;
    }



}

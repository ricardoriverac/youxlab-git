package com.libraryAtividade.libraryAtividade.repositories;

import com.libraryAtividade.libraryAtividade.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface BookRepository extends JpaRepository<Book, UUID> {
}

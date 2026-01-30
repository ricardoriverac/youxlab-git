package com.example.libraryapi.repository;

import com.example.libraryapi.model.Livro;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface LIvroRepository extends JpaRepository<Livro, UUID> {
}

package com.libraryAtividade.libraryAtividade.dto;



import java.util.Date;

public record BookDTO(String titulo, String autor, Date anoPublicacao, String isbn, Boolean Disponibility) {


}

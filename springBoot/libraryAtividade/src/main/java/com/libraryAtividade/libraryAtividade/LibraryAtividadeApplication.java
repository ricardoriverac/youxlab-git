package com.libraryAtividade.libraryAtividade;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
public class LibraryAtividadeApplication {
	public static List<Integer> contagem(){
		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < 10; i ++){
			list.add(i);

		}
		System.out.println(list);
		return list;
	}

	public static void main(String[] args) {
		SpringApplication.run(LibraryAtividadeApplication.class, args);
		contagem();
	}

}

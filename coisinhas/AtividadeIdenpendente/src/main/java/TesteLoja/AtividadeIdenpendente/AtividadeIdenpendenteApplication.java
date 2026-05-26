package TesteLoja.AtividadeIdenpendente;

import TesteLoja.AtividadeIdenpendente.components.entities.User;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

@SpringBootApplication

public class AtividadeIdenpendenteApplication {

	private static List<Integer> contagem(){
		List<Integer> number = new ArrayList<>();

		for (int i = 0; i < 10; i ++) {
			number.add(i);
		}
		return number;
	}

	public static void main(String[] args) {
		SpringApplication.run(AtividadeIdenpendenteApplication.class, args);
		System.out.println(contagem());
	}


}

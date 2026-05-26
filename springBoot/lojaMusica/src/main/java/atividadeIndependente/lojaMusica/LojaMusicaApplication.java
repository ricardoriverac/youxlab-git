package atividadeIndependente.lojaMusica;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
public class LojaMusicaApplication {

	public static void contagem(){
		List<Integer> lista = new ArrayList<>();
		for (Integer i = 0 ; i < 10 ; i++){
			lista.add(i);
		}
		System.out.println(lista);
	}

	public static void main(String[] args) {
		SpringApplication.run(LojaMusicaApplication.class, args);
		contagem();
	}

}

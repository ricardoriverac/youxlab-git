package io.TesteLucas.libraryapi2;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
@EnableJpaAuditing
public class Libraryapi2Application {

	public static void contagem(){
		List<Double> list = new ArrayList<>();
		for(Double i = 0.0; i < 10; i++){
			list.add(i);
		}
		System.out.println(list);
	}

	public static void main(String[] args) {
		SpringApplication.run(Libraryapi2Application.class, args);
		contagem();
	}

}

package com.example.librayapi;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

import java.time.LocalDate;

@SpringBootApplication
@EnableJpaAuditing
public class LibrayapiApplication {

	public static void main(String[] args) {
        SpringApplication.run(LibrayapiApplication.class, args);

	}

}

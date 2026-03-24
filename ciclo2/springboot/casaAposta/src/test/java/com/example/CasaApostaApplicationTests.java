package com.example;

import com.example.dto.UserRequestDTO;
import com.example.service.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDate;

@SpringBootTest
class CasaApostaApplicationTests {

	@Autowired
	UserService userService;

	@Test
	void contextLoads() {
	}

	@Test
	void cadastro() {
		userService.criarAdmin(new UserRequestDTO( "DaniAdm",  "dani@email.com", LocalDate.now(),  "1234Asd@",  "1234Asd@"));
	}

}

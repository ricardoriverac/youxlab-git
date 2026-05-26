package com.example.ecommerce;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
public class EcommerceApplication {
	public static void contando(){
		List<Double> list = new ArrayList<>();
		for(Double i = 0.00; i < 10; i++){
			list.add(i);
		}

		System.out.println(list);
	}
	public static void main(String[] args) {
		SpringApplication.run(EcommerceApplication.class, args);
		contando();
	}

}

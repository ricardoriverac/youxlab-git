package io.github.cursodsousa.arquiteturaSpring;

import org.springframework.boot.Banner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.core.env.ConfigurableEnvironment;

@SpringBootApplication
public class ArquiteturaSpringApplication {

	public static void main(String[] args) {


		SpringApplicationBuilder builder =
				new SpringApplicationBuilder(ArquiteturaSpringApplication.class);
		builder.bannerMode(Banner.Mode.OFF);
		builder.profiles("producao");

		builder.run(args);

		ConfigurableApplicationContext applicationContext = builder.context();
		//SpringApplication.run(ArquiteturaSpringApplication.class, args);

		ConfigurableEnvironment environment = applicationContext.getEnvironment();
		String applicationName = environment.getProperty("spring.application.name");
		System.out.println("Nome da aplicação: " + applicationName);

		ExemploValue value = applicationContext.getBean(ExemploValue.class);
		value.imprimirVariavel();

		AppProperties valor1 = applicationContext.getBean(AppProperties.class);
		System.out.println(valor1.getValor1());;
	}

}

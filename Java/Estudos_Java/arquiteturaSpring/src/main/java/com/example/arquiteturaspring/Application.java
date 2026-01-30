package com.example.arquiteturaspring;

import org.springframework.boot.Banner;
import org.springframework.boot.ConfigurableBootstrapContext;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.core.env.ConfigurableEnvironment;

@SpringBootApplication
@EnableConfigurationProperties
public class Application {

	public static void main(String[] args) {
		//SpringApplication.run(Application.class, args);

		SpringApplicationBuilder builder =
				new SpringApplicationBuilder(Application.class);

		builder.bannerMode(Banner.Mode.OFF);
		builder.properties("producao", "homologacao");
//		builder.lazyInitialization(true);

		builder.run(args);

		ConfigurableApplicationContext applicationContext = builder.context();
		ConfigurableEnvironment environment = applicationContext.getEnvironment();

		ExemploValue value = applicationContext.getBean(ExemploValue.class);
		value.imprimirVariavel();

		AppProperties properties = applicationContext.getBean(AppProperties.class);
		System.out.println(properties.getValor1());
	}

}

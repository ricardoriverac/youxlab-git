package io.github.cursodsousa.arquiteturaSpring.montadora.configuration;


import io.github.cursodsousa.arquiteturaSpring.montadora.Motor;
import io.github.cursodsousa.arquiteturaSpring.montadora.TipoMotor;
import io.github.cursodsousa.arquiteturaSpring.montadora.annotations.Aspirado;
import io.github.cursodsousa.arquiteturaSpring.montadora.annotations.Eletrico;
import io.github.cursodsousa.arquiteturaSpring.montadora.annotations.Turbo;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MontadoraConfiguration {
    //Para definir um bean padrão entre outros beans de mesmo tipo, basta usar @Primary

    @Bean
    //Utilizando uma Annotation personalizada para definir o TIPO de bean do método
    //Também podemos utilizar @Qualifier(name = "x") para definir o TIPO de bean
    @Aspirado
    public Motor motor(){
        var motor = new Motor();
        motor.setCavalos(120);
        motor.setCilindros(4);
        motor.setModelo("XPTO-G");
        motor.setLitragem(2.0);
        motor.setTipo(TipoMotor.ASPIRADO);
        return motor;
    }
    @Bean
    @Eletrico
    public Motor motorEletrico(){
        var motor = new Motor();
        motor.setCavalos(110);
        motor.setCilindros(3);
        motor.setModelo("TH-40");
        motor.setLitragem(1.4);
        motor.setTipo(TipoMotor.ELETRICO);
        return motor;
    }
    @Bean
    @Turbo
    public Motor motorTurbo(){
        var motor = new Motor();
        motor.setCavalos(180);
        motor.setCilindros(4);
        motor.setModelo("XPTO-01");
        motor.setLitragem(2.0);
        motor.setTipo(TipoMotor.TURBO);
        return motor;
    }
}

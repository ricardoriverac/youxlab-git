package Aula_118.Instanciando_data_hora;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class Aula_01 {
    public static void main(String[] args) {

        //Formata datas e horas
        DateTimeFormatter fmt1 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

        //Printa somente a data do computador (Ano-Mes-Dia)
        LocalDate d01 = LocalDate.now();
        System.out.println(d01);

        //Printa as horas do computador (Hora:Minuto:Segundo.microsegundos)
        LocalTime d03 = LocalTime.now();
        System.out.println(d03);

        //Printa a data e as horas do computador (Ano-Mes-DiaTHora:Minuto:Segundo.microsegundos)
        LocalDateTime d02 = LocalDateTime.now();
        System.out.println(d02);

        //Printa a data e as horas de Greenwich (Ano-Mes-DiaTHora:Minuto:Segundo.microsegundos)
        Instant d04 = Instant.now();
        System.out.println(d04);

       //Coverte string para date (coverte somente string com data como valor!)
        LocalDate d05 = LocalDate.parse("2010-05-08");
        LocalDateTime d06 = LocalDateTime.parse("2010-05-08T01:30:26");
        Instant d07 = Instant.parse("2010-05-08T01:30:26Z");

        System.out.println(d05);
        System.out.println(d06);
        System.out.println(d07);

        //Data e Hora formatado
        LocalDateTime d08 = LocalDateTime.parse("04/01/2009 22:34", fmt1);
        System.out.println(d08);

        //Istancia ano, mes e dia separadamente
        LocalDate d09 = LocalDate.of(2022, 7, 20);
        System.out.println(d09);

        //Istancia Ano, mes e dia separadamente
        LocalDateTime d10 = LocalDateTime.of(2022, 7, 20, 1, 30);
        System.out.println(d10);

    }
}

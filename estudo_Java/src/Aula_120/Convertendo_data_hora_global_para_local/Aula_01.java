package Aula_120.Convertendo_data_hora_global_para_local;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;

public class Aula_01 {
    public static void main(String[] args) {

        LocalDate d04 = LocalDate.parse("2022-07-20");
        LocalDateTime d05 = LocalDateTime.parse("2022-07-20T01:30:26");
        Instant d06 = Instant.parse("2022-07-20T01:30:26Z");

        // Converte o Instant (UTC) para a data no fuso horário padrão do computador
        LocalDate r1 = LocalDate.ofInstant(d06, ZoneId.systemDefault());

        // Converte o mesmo Instant (UTC) para a data no fuso horário de Portugal
        LocalDate r2 = LocalDate.ofInstant(d06, ZoneId.of("Portugal"));

        System.out.println(r1);
        System.out.println(r2);

        // Converte o Instant (UTC) para data e hora no fuso horário do computador
        LocalDateTime r3 = LocalDateTime.ofInstant(d06, ZoneId.systemDefault());

        // Converte o mesmo Instant (UTC) para data e hora no fuso horário de Portugal
        LocalDateTime r4 = LocalDateTime.ofInstant(d06, ZoneId.of("Portugal"));

        System.out.println(r3);
        System.out.println(r4);

        //Printa somente a o dia da data
        System.out.println(d04.getDayOfMonth());

        //printa somente o mes da data
        System.out.println(d04.getMonthValue());

        //Printa somente o ano da data
        System.out.println(d04.getYear());

        //Printa a hora
        System.out.println(d05.getHour());

        //Printa os minutos
        System.out.println(d05.getMinute());

        //Printa os segundos
        System.out.println(d05.getSecond());

        //Retorna um conjunto de textos com todos os nomes de fusos horários que o Java conhece.
        for (String s : ZoneId.getAvailableZoneIds()) {
            System.out.println(s);
        }

    }
}

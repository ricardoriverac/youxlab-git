package Aula_119.Convertendo_data_hora_para_texto;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

public class Aula_01 {
    public static void main(String[] args) {

        LocalDate d04 = LocalDate.parse("2022-07-20");
        LocalDateTime d05 = LocalDateTime.parse("2022-07-20T01:30:26");
        Instant d06 = Instant.parse("2022-07-20T01:30:26Z");

        DateTimeFormatter fmt1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter fmt2 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        DateTimeFormatter fmt3 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm").withZone(ZoneId.systemDefault());

        //1º forma de printar a data do mesmo jeito que a formatação
        System.out.println(d04.format(fmt1));

        //2º forma de printar a data do mesmo jeito que a formatação
        System.out.println(fmt1.format(d04));

        //3º forma de printar a data do mesmo jeito que a formatação
        System.out.println(d04.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));

        //Printa a data e a hora da mesma forma que a formatação
        System.out.println(d05.format(fmt2));

        //Printa a hora e data do fusorario de Greenwich do mesma forma da formatação
        System.out.println(fmt3.format(d06));

    }
}

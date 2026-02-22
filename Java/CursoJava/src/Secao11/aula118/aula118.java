package Secao11.aula118;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class aula118 {
    public static void main(String[] args) {
        LocalDate d01 = LocalDate.now();
        LocalTime d02 = LocalTime.now();
        Instant d03 = Instant.now();

        System.out.println("d01 = "+ d01);
        System.out.println("d02 = "+ d02);
        System.out.println("d03 = "+ d03);



    }
}

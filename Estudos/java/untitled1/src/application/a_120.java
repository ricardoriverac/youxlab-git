package application;

import java.time.Duration;
import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.Locale;

public class a_120 {
    public static void main(String[] args) {
        LocalDate d01 = LocalDate.parse("2022-07-20");
        LocalDateTime d02 = LocalDateTime.parse("2022-07-20T01:30:26");
        Instant d03 = Instant.parse("2022-07-20T01:30:26Z");

        LocalDate pastWeekDate = d01.minusDays(7);
        LocalDate nextWeekDate = d01.plusDays(7);

        LocalDateTime pastWeekLocalDate = d02.minusDays(7);
        LocalDateTime nextWeekLocalDate = d02.plusDays(7);

        Instant pastWeekInstant = d03.minus(7, ChronoUnit.DAYS);
        Instant nextWeekInstant = d03.plus(7, ChronoUnit.DAYS);

        System.out.println(pastWeekDate);
        System.out.println(nextWeekDate);

        System.out.println(pastWeekLocalDate);
        System.out.println(nextWeekLocalDate);

        System.out.println(pastWeekInstant);
        System.out.println(nextWeekInstant);

        Duration t1 = Duration.between(pastWeekDate.atStartOfDay(), nextWeekDate.atStartOfDay());
        Duration t2 = Duration.between(pastWeekLocalDate, d02);
        Duration t3 = Duration.between(pastWeekInstant, d03);
        Duration t4 = Duration.between(d03, pastWeekInstant);

        System.out.println(t1);
        System.out.println(t2);
        System.out.println(t3);
        System.out.println(t4);


    }
}

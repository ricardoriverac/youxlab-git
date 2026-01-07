package curso_completo_java.sessao_11.pratica;

// AULA - 123 - Manipulando um Date com Calendar

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Calendar;
import java.util.Date;

public class exemplo_pratica06 {

    public static void main(String[] args) throws ParseException {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");

        Date d = Date.from(Instant.parse("2018-06-25T15:42:07Z"));

        System.out.println(sdf.format(d));

        Calendar cal = Calendar.getInstance();
        cal.setTime(d);
        cal.add(Calendar.HOUR_OF_DAY, 4);

        d = cal.getTime();
        System.out.println(sdf.format(d));
    }


    }





package Date.DateComCalender;

import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Calendar;
import java.util.Date;

public class Manipulando {
    static void main() {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        Date d = Date.from(Instant.parse("2018-06-25T15:42:07Z"));
        System.out.println(sdf.format(d));

        Calendar cal = Calendar.getInstance();
        cal.setTime(d);


         // AUMENTANDO HORAS DO DIA
         cal.add(Calendar.HOUR_OF_DAY, 4);
         d = cal.getTime();


         // vendo MINUTOS E HORAS
        int minutes = cal.get(Calendar.MINUTE);
        int month = 1 + cal.get(Calendar.MONTH);

        System.out.println("+ 4 horas = " + sdf.format(d));
        System.out.println("Minutes = " +  minutes);
        System.out.println("Month = " +  month);

    }
}

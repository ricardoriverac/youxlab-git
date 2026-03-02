package Secao_11.Aula_124.Manipulando_date_com_Calendar;

//Titulo: Somando uma unidade de tempo

import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Calendar;
import java.util.Date;

public class Aula_01 {
    public static void main(String[] args) {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");

        Date d = Date.from(Instant.parse("2018-06-25T15:42:07Z"));

        System.out.println(sdf.format(d));

        Calendar cal = Calendar.getInstance();

        //Istancia o valor do objeto d(Date) para dentro do objeto cal(Calendar)
        cal.setTime(d);

        // Soma 4 horas ao horário do Calendar, ajustando o dia automaticamente se necessário.
        cal.add(Calendar.HOUR_OF_DAY, 4);//87672 - 10 anos no futuro

        // Obtém a data do Calendar como Date e guarda em d.
        d = cal.getTime();

        System.out.println(sdf.format(d));
    }
}

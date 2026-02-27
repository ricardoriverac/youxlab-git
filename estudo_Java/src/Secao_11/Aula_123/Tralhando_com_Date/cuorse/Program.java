package Secao_11.Aula_123.Tralhando_com_Date.cuorse;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Date;
import java.util.Scanner;
import java.util.TimeZone;

public class Program {
    public static void main(String[] args) throws ParseException {

        Scanner sc = new Scanner(System.in);

        //São objetos formatador de datas, define um padrão para datas
        SimpleDateFormat sdf1 = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat sdf2 = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        SimpleDateFormat sdf3 = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");

        // Define o fuso GMT para exibição da data (não altera o valor interno)
        sdf3.setTimeZone(TimeZone.getTimeZone("GMT"));

        //Converte String para Date e depois atribuí à variável
        Date y1 = sdf1.parse("25/06/2018");
        Date y2 = sdf2.parse("25/06/2018 15:42:07");
        Date y3 = (Date.from(Instant.parse("2018-06-25T15:42:07Z")));

        System.out.println("y1: " + sdf1.format(y1));
        System.out.println("y2: " + sdf2.format(y2));
        System.out.println("y3: " + sdf2.format(y3));

        //Pega a data atual da maquina e guarda no objeto
        Date x1 = new Date();
        System.out.println("x1: " + sdf2.format(x1));

        //Pega milissegundos desde 1970 e converte para Date
        Date x2 = new Date(System.currentTimeMillis());
        System.out.println("x2: " + sdf2.format(x2));

        //Cria um objeto Date baseado nos milissegundos desde 1970
        Date x3 = new Date(995694345345L);
        System.out.println("x3: " + sdf2.format(x3));

        //5 horas depois de 1970
        Date x4 = new Date(1000L * 60L * 60L * 5L);
        System.out.println("x4: " + sdf2.format(x4));

        System.out.println("============= FORMATAÇÃO GNT ================");
        System.out.println("y1: " + sdf3.format(y1));
        System.out.println("y2: " + sdf3.format(y2));
        System.out.println("y3: " + sdf3.format(y3));
        System.out.println("x1: " + sdf3.format(x1));
        System.out.println("x2: " + sdf3.format(x2));
        System.out.println("x3: " + sdf3.format(x3));
        System.out.println("x4: " + sdf3.format(x4));
        System.out.println("============= SEM FORMATAÇÃO ================");
        System.out.println("y1: " + y1);
        System.out.println("y2: " + y2);
        System.out.println("y3: " + y3);
        System.out.println("x1: " + x1);
        System.out.println("x2: " + x2);
        System.out.println("x3: " + x3);
        System.out.println("x4: " + x4);
    }
}

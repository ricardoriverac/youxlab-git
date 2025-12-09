package secao_06;

import java.awt.*;
import java.util.Locale;
import java.util.Scanner;

public class exercicio3for {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int casos_teste = sc.nextInt();
        int peso = 2;
        int peso2= 3;
        int peso3 = 5;

        for (int i=0; i<casos_teste; i++) {

            double notas1 = sc.nextDouble();
            double notas2 = sc.nextDouble();
            double notas3 = sc.nextDouble();

            double media = (notas1 * peso + notas2 * peso2 + notas3 * peso3) / 10.0;

            System.out.printf("%.1f%n", media);
        }

        sc.close();

    }
}

package secao6_estruturasRepetitivas.atividadesFor;

import java.util.Locale;
import java.util.Scanner;

public class exercicio3 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        double a = 0;
        double b = 0;
        double c = 0;
        double media = 0;
        for(int i=0; i < n; i++) {
            a = sc.nextDouble();
            b = sc.nextDouble();
            c = sc.nextDouble();
            media = (a + b + c)/3;
            System.out.println(media);
        }

    }
}

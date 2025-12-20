package secao_08.EXerciciosDefixacao;

import java.util.Locale;
import java.util.Scanner;

public class exerci01A77 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("What is the dollar price? ");
        double vallueDolar = sc.nextDouble();

        System.out.println("How many dollars will be bougth? ");
        double bougthdollar = sc.nextDouble();

        System.out.printf("Amount to be paind in reais =  %.2f", CurrencyConverter.dollarToReal(vallueDolar, bougthdollar) );
    }
}

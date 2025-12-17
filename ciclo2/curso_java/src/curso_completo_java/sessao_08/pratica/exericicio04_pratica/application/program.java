package curso_completo_java.sessao_08.pratica.exericicio04_pratica.application;

import curso_completo_java.sessao_08.pratica.exericicio04_pratica.etities.CurrencyConverter;

import java.util.Locale;
import java.util.Scanner;

public class program {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            System.out.print("What is the dollar price? ");
            double dollarPrice = sc.nextDouble();

            System.out.print("How many dollars will be bought? ");
            double amount = sc.nextDouble();

            double resultado = CurrencyConverter.amountPaid(dollarPrice, amount);

            System.out.printf("Amount to be paid in reais = %.2f%n", resultado);

            sc.close();
        }
    }



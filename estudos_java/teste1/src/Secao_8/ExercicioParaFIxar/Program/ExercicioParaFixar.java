package Secao_8.ExercicioParaFIxar.Program;

import Secao_8.ExercicioParaFIxar.Calculator.CurrencyCalculator;

import java.util.Locale;
import java.util.Scanner;

public class ExercicioParaFixar {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("What is the dollar price? ");
        double dollarPrice = sc.nextDouble();

        System.out.println("How many dollars will be bought? ");
        double dollar = sc.nextDouble();

        System.out.printf("Amount to be paid in reais = %.2f", CurrencyCalculator.convertRealToDollar(dollar,dollarPrice));
    }
}

package Programacao_Orientada_Objetos.Membros_Estaticos.ExercicioDeFixacao.application;

import Programacao_Orientada_Objetos.Membros_Estaticos.ExercicioDeFixacao.util.CurrencyConverter;
import Programacao_Orientada_Objetos.Membros_Estaticos.util.Calculator;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("What is the dollar price? ");
        double valueDollar = sc.nextDouble();

        System.out.print("How many dollars will be bought? ");
        double boughtDollars = sc.nextDouble();

        System.out.printf("Amount to be paid in reais = %.2f", CurrencyConverter.boughtReais(valueDollar, boughtDollars));

    }
}

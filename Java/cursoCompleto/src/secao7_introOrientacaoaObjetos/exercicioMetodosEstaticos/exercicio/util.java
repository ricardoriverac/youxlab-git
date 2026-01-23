package secao7_introOrientacaoaObjetos.exercicioMetodosEstaticos.exercicio;

import secao7_introOrientacaoaObjetos.exercicioMetodosEstaticos.metodo.met;
import java.util.Locale;
import java.util.Scanner;

public class util {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        System.out.print("What is the dollar price? ");
        double dollarPrice = sc.nextDouble();
        System.out.print("How many dollars will be bought? ");
        double amount = sc.nextDouble();
        double result = met.calcularDol(amount, dollarPrice);
        System.out.printf("Amount to be paid in reais = %.2f%n", result);
        sc.close();
    }
}
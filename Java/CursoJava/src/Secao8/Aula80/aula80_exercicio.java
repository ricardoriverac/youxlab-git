package Secao8.Aula80;

import java.util.Locale;
import java.util.Scanner;

public class aula80_exercicio {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("What is the dollar price? ");
        double cotacao = sc.nextDouble();
        System.out.print("How many dollars will be bought? ");
        double valordolar = sc.nextDouble();
        double taxaiof = 0.06;
        double valorsemiof = valordolar * cotacao;
        double valoriof = valorsemiof * taxaiof;
        double valorFinal = valorsemiof + valoriof;
        System.out.printf("Amount to be paid in reais = R$ %.2f%n", valorFinal);

        sc.close();
    }
}

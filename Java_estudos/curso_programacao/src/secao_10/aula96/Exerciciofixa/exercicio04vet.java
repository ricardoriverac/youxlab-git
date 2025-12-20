package secao_10.aula96.Exerciciofixa;

import java.util.Locale;
import java.util.Scanner;

public class exercicio04vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Quantos números você quer digitar? ");
        int numerosDigitar = sc.nextInt();
        double[] digitados = new double[numerosDigitar];

        for (int i = 0; i < numerosDigitar; i++) {
            System.out.println("Digite um número: ");
            digitados[i] = sc.nextDouble();
        }
        System.out.println("VALRES: ");

        for (int i = 0; i < digitados.length; i++) {
            System.out.println(digitados[i] + ",");

        }
        double soma = 0;

        for (int i = 0; i < numerosDigitar; i++) {
             soma += digitados[i];
        }
        System.out.println(soma);
        System.out.println("MEDIA");

        double media = 0;
        for (int i = 0; i < numerosDigitar; i++) {
            media += media + digitados[i];
        }
        media = media / numerosDigitar;
        System.out.printf("%.2f%n" , media);



    }
}

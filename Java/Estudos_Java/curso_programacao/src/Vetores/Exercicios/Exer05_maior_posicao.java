package Vetores.Exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Exer05_maior_posicao {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números você vai digitar? ");
        int qntNumeros = sc.nextInt();
        double[] numeros = new double[qntNumeros];

        for (int i = 0; i < qntNumeros; i++) {
            System.out.print("Digite um número: ");
            numeros[i] = sc.nextDouble();
        }


        double maior = numeros[0];
        int indiceMaior =0;
        for (int i = 0; i < numeros.length; i++) {
           if (numeros[i] > maior) {
               maior = numeros[i];
               indiceMaior = i;
           }
        }

        System.out.println("POSICAO DO MAIOR NÚMERO: " + indiceMaior);
        System.out.print("MAIOR VALOR = " + maior);




        sc.close();
    }
}

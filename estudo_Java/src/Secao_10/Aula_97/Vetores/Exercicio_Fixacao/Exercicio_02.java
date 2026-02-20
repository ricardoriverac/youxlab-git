package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Scanner;

public class Exercicio_02 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos numeros voce vai digitar: ");
        int n = sc.nextInt();

        int[] valores = new int[n];

        for (int i=0; i<n; i++) {
            System.out.print("Digite um numero: ");
            valores[i] = sc.nextInt();
        }

        System.out.print("VALORES = ");

        for (int i=0; i<valores.length; i++) {
            System.out.print(valores[i] + " ");
        }

        int sum = 0;
        for (int i=0; i<valores.length; i++) {
            sum = sum + valores[i];
        }


        System.out.printf("%nSOMA = %d %n", sum);

        int media = sum / n;

        System.out.println("MEDIA = " + media);

    }
}

package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex7 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, quantos elementos você deseja verificar? ");
        int quantidadeValores = sc.nextInt();
        double[] numeros = new double[quantidadeValores];

        for (int i = 0; i < numeros.length; i++) {
            System.out.printf("Caro usuário, por favor insira o %do valor: ", i+1);
            numeros[i] = sc.nextDouble();
        }
        double soma = 0.0;
        for (int i = 0; i <numeros.length; i++) {
            soma += numeros[i];
        }
        System.out.printf("Média do vetor: %.3f\n", soma/ numeros.length);
        System.out.println("Valores abaixo da média: ");
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] < soma/numeros.length){
                System.out.println(numeros[i]);
            }

        }
    }
}

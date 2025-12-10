package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex8 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, quantos valores você deseja verificar? ");
        int quantidadeValores = sc.nextInt();
        double[] numeros = new double[quantidadeValores];

        for (int i = 0; i < numeros.length; i++) {
            System.out.printf("Caro usuário, por favor insira seu %do valor do seu vetor: ", i+1);
            numeros[i] = sc.nextDouble();
        }
        double soma = 0.0;
        int countPares = 0;
        for (int i = 0; i < numeros.length; i++) {
            if(numeros[i] % 2 == 0){
                soma+= numeros[i];
                countPares+=1;
            }
        }
        if(countPares == 0){
            System.out.print("Nenhum número par inserido! ");
        }
        else {
            System.out.printf("Média dos valores pares: %.2f", soma / countPares);
        }
    }
}

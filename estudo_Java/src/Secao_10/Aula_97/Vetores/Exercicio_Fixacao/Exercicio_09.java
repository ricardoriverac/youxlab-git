package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Scanner;

public class Exercicio_09 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Quantas pessoas voce vai digitar: ");
        int n = sc.nextInt();

        int cont = 0;

        String[] vetorNome = new String[n];
        int[] vetorIdade = new int[n];

        for (int i=0; i<n; i++) {
            cont++;
            System.out.printf("Dados da %d° pessoa", cont);

            System.out.print("Nome: ");
            vetorNome[i] = sc.next();

            System.out.print("Idade: ");
            vetorIdade[i] = sc.nextInt();
        }

        int posicaoMaisVelha = 0;

        for (int i = 1; i < n; i++) {
            if (vetorIdade[i] > vetorIdade[posicaoMaisVelha]) {
                posicaoMaisVelha = i;
            }
        }

        System.out.println("PESSOA MAIS VELHA: " + vetorNome[posicaoMaisVelha]);



    }
}

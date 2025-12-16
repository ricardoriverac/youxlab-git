package Vetores.Exercicios;

import java.util.Scanner;

public class Exer09_maisVelhos {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantas pessoas irá digitar? ");
        int qntPessoas= sc.nextInt();
        int[] vetorIdade = new int[qntPessoas];
        String[] vetorNome = new String[qntPessoas];

        for (int i = 0; i < qntPessoas; i++) {
            System.out.println("Dados da " + (i+1) + "a pessoa:");
            System.out.print("Nome: ");
            vetorNome[i]= sc.next();
            System.out.print("Idade: ");
            vetorIdade[i] = sc.nextInt();
        }


        int indice = 0;
        int idadeMaisVelha = vetorIdade[0];
        for (int i = 0; i < qntPessoas; i++) {
            if (vetorIdade[i] > idadeMaisVelha){
                idadeMaisVelha = vetorIdade[i];
                indice = i;
            }
        }

        System.out.println("PESSOA MAIS VELHA: " + vetorNome[indice]);


        sc.close();
    }
}

package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex3 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, por favor insira quantas pessoas você deseja cadastrar: ");
        int quantidadePessoas = sc.nextInt();

        String[] nome = new String[quantidadePessoas];
        int[] idade = new int[quantidadePessoas];
        double[] altura = new double[quantidadePessoas];
        double soma = 0.0;

        for (int i = 0; i < quantidadePessoas; i++) {
            System.out.printf("Caro usuário, por favor insira o nome da %da pessoa que você deseja cadastrar: \n", i+1);
            sc.nextLine();
            nome[i] = sc.nextLine();
            System.out.print("Caro usuário, por favor insira a idade desta pessoa: \n");
            idade[i] = sc.nextInt();
            System.out.print("Caro usuário, por favor insira a altura desta pessoa: \n");
            altura[i] = sc.nextDouble();
            soma+= altura[i];
            System.out.printf("Dados da %da  pessoa:\n Nome: %s\n Idade: %d\n Altura: %.2f\n", i+1,nome[i], idade[i], altura[i]);
        }


        int contador_menor_de_idade = 0;
        for (int i = 0; i < quantidadePessoas; i++) {
            if (idade[i] < 16){
                contador_menor_de_idade += 1;
            }
        }
        double avgAltura = soma / quantidadePessoas;
        System.out.printf("Altura média: %.2f\n", avgAltura);
        if (contador_menor_de_idade != 0) {
            double menor16 = ((double) contador_menor_de_idade / quantidadePessoas) * 100;

            System.out.printf("Pessoas com menos de 16 anos: %.2f%%\n", menor16);
        }
        else{
            System.out.println("Sem pessoas menores de 16 anos cadastradas");
        }
        for (int i = 0; i < quantidadePessoas; i++) {
            if(idade[i] < 16){
                System.out.printf("%s\n", nome[i]);
            }

        }

    }
}

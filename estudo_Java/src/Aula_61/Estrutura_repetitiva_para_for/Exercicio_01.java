package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Scanner;

public class Exercicio_01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um valor: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++){
            if (i % 2 != 0){
                System.out.println(i);
            }
        }

    }
}
package Aula_56.Estrutura_repetitiva_enquanto_while;

import java.util.Scanner;

public class Aula_01 {
    public static void main(String[] args) {

        System.out.print("Digite um valor de 0 a 5: ");
        Scanner sc = new Scanner(System.in);

        int valor = sc.nextInt();

        while (valor != 0){
            System.out.print("Digite um valor de 0 a 5: ");
            valor = sc.nextInt();

        }
        System.out.println("Você acertou!!");
    }
}
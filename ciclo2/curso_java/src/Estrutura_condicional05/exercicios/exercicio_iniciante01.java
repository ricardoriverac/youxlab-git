package Estrutura_condicional05.exercicios;

/* Fazer um programa para ler um número inteiro, e depois dizer
se este número é negativo ou não. */

import java.util.Scanner;

    public class exercicio_iniciante01 {

	    public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        System.out.println("Digite um número inteiro: ");
		int Numero = sc.nextInt();

		if (Numero < 0) {
			System.out.println("Negativo");
		}
		else {
			System.out.println("Não negativo");
		}

		sc.close();
	}
}


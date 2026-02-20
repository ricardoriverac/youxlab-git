package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Scanner;

public class Exercicio_04 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int c = 0;

        System.out.print("Quantos numeros voce vai digitar? ");
        int n = sc.nextInt();

        int[] vect = new int[n];
        int[] vectPar = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Digite um numero: ");
            vect[i] = sc.nextInt();

            if (vect[i] % 2 == 0) {
                c++;
                vectPar[i] = vect[i];
            }
        }

        System.out.print("NUMEROS PARES: ");
        for (int i = 0; i < vectPar.length; i++) {
            if (vectPar[i] != 0) System.out.print(vectPar[i]  +    " ");

        }
        System.out.printf("%nQUATIDADE DE PARES = %d", c);
    }
}

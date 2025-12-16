package secao_10.Aula_96.Exerciciofixa.EntitiesA97E03;

import java.util.Locale;
import java.util.Scanner;

public class exercicio05vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Quantos numeros voce vai digitar? ");
        int dgtNum = sc.nextInt();
        int[] vect = new int[dgtNum];


        for (int i = 0; i < dgtNum; i++) {
            System.out.println("Digite um numero ");
            vect[i] = sc.nextInt();
        }

        System.out.println("Numeros pares: ");
         int numerospares = 0;

        for (int i = 0; i < dgtNum; i++) {
            if (vect[i] % 2 == 0 ){
                numerospares++;
                System.out.println(vect[i] + " ");
            }

        }
        System.out.println();
        System.out.println("Quantidade de pares: " +  numerospares);


        sc.close();
    }
}

package secao9_Java.exerciciosFixacaoVetores.aplicacao;

import java.util.Scanner;
import secao9_Java.exerciciosFixacaoVetores.produto.metodos1;

public class aplicacao1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int [] numerosLista = new int[n];
        for (int i = 0; i < n; i++) {
            numerosLista[i] = sc.nextInt();
        }
        System.out.println("NUMEROS NEGATIVOS");

        for (int i =0; i<n; i++) {
            if (numerosLista[i] < 0) {
                System.out.printf("%d\n", numerosLista[i]);
            }
        }
    }
}

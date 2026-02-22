package Secao10.Aula98.exercicio1;

import java.util.Locale;
import java.util.Scanner;
import java.util.concurrent.locks.Lock;

public class program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("quantos numeros voce vai digitar? ");
        int n = sc.nextInt();

        int[] vet = new int[n];
        for (int i = 0; i<n; i++) {
            System.out.print("Digite um número: ");
            vet[i] = sc.nextInt();
        }
        System.out.print("Números negativos: ");
        for (int i = 0; i<n; i++) {
            if (vet[i] < 0) {
                System.out.println(vet[i]);
            }
            }
        sc.close();
        }
    }
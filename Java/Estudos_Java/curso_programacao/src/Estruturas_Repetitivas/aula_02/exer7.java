package Estruturas_Repetitivas.aula_02;

import java.util.Scanner;

public class exer7 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int numero = sc.nextInt();
        for (int i = 1; i<=numero; i++){
            int primeiro = i;
            int ao_quadrado = i * i;
            int ao_cubo = i * i * i;
            System.out.printf("%d %d %d%n", primeiro, ao_quadrado, ao_cubo);
        }
        sc.close();
    }
}

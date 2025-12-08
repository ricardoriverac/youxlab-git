package Estrutura_Sequencial.aula_03;

import java.util.Locale;
import java.util.Scanner;

public class exer2 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double R, A, pi;
        R = sc.nextDouble();
        pi = 3.14159;

        A = pi * R * R;
        System.out.printf("A = %.4f%n ", A);
    }
}

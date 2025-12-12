package Estrutura_Sequencial.aula_03;

import java.util.Locale;
import java.util.Scanner;

public class exer3 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int A, B, C, D;
        int diferenca;
        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        D = sc.nextInt();

        diferenca = (A * B - C * D);
        System.out.println("Diferença = " + diferenca);
    }
}

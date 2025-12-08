package Estrutura_Sequencial.aula_03;

import java.util.Locale;
import java.util.Scanner;

public class exer6 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double A, B, C;
        double TRI, CIR, TRA, QUA, RETAN;

        A = sc.nextDouble();
        B = sc.nextDouble();
        C = sc.nextDouble();

        TRI = (A * C) / 2.0;
        CIR = 3.14159 * C * C;
        TRA = (A + B) * C / 2.0;
        QUA = (B * B);
        RETAN = A * B;

        System.out.printf("Triangulo = %.3f%n", TRI);
        System.out.printf("Circulo = %.3f%n", CIR);
        System.out.printf("Trapezio = %.3f%n", TRA);
        System.out.printf("Quadrado = %.3f%n", QUA);
        System.out.printf("Retangulo = %.3f%n", RETAN);
    }
}

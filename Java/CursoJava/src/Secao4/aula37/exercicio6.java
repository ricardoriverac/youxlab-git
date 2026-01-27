package Secao4.aula37;

import javax.swing.plaf.synth.SynthTextAreaUI;
import java.util.Locale;
import java.util.Scanner;

public class exercicio6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        double A, B, C, trian, tra,qua, circ, retan;
        A = sc.nextDouble();
        C = sc.nextDouble();
        B = sc.nextDouble();
        trian = A * C / 2.0;
        circ = Math.PI * Math.pow(3.14159, 2);
        tra = A + B * C;
        qua = C * C;
        retan = A * C;

        System.out.printf("Triangulo: %.3f\n", trian);
        System.out.printf("Circulo: %.3f\n", circ);
        System.out.printf("Trapezio: %.3f\n", tra);
        System.out.printf("Quadrado: %.3f\n", qua);
        System.out.printf("Retangulo: %.3f\n", retan);

        sc.close();
    }
}

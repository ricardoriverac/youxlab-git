package Secao4.aula37;

import javax.swing.plaf.synth.SynthTextAreaUI;
import java.util.Locale;
import java.util.Scanner;

public class exercicio6 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double A, B, C, trian, tra,qua, circ, retan;
        A = sc.nextDouble();
        B = sc.nextDouble();
        C = sc.nextDouble();
        trian = (A * C) / 2.0;
        circ = Math.PI * Math.pow(C, 2);
        tra = ((A + B) * C )/2;
        qua = B * B;
        retan = A * B;

        System.out.printf("Triangulo: %.3f\n", trian);
        System.out.printf("Circulo: %.3f\n", circ);
        System.out.printf("Trapezio: %.3f\n", tra);
        System.out.printf("Quadrado: %.3f\n", qua);
        System.out.printf("Retangulo: %.3f\n", retan);

        sc.close();
    }
}

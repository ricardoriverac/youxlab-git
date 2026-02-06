package Secao7.Aula67;
/*
     Este programa calcula as raízes de uma equação do segundo grau

     Os valores coeficientes devem ser digitados um por linha
      */

import java.util.Locale;
import java.util.Scanner;

public class aula67 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double a, b, c, delta;

        System.out.println("Digite os valores dos coeficientes: ");
        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();

        delta = b * b - 4 * a * c;

        System.out.println(delta);

        sc.close();
    }
}

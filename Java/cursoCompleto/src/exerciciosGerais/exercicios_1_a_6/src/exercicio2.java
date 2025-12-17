package exerciciosGerais.exercicios_1_a_6.src;

import java.util.Scanner;
import static java.lang.Math.pow;

public class exercicio2  {
    public static void main(String[] args){
        double pi, area, raio;

        Scanner sc = new Scanner(System.in);
        raio = sc.nextDouble();
        pi = 3.14159;
        area = pow(raio, 2) * pi;
        System.out.println("A área é " + area);
        sc.close();
    }

}
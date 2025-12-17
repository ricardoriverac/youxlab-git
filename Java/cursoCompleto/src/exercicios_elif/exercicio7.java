package exercicios_elif;

import java.util.Locale;
import java.util.Scanner;

public class exercicio7 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double eixoX = sc.nextDouble();
        double eixoY = sc.nextDouble();

        if (eixoX > 0 && eixoY > 0) {
            System.out.println("Quadrante 1");
        }
        else if (eixoX < 0 && eixoY > 0) {
            System.out.println("Quadrante 2");
        }
        else if (eixoX < 0 && eixoY < 0) {
            System.out.println("Quadrante 3");
        }
        else if (eixoX > 0 && eixoY < 0){
            System.out.println("Quadrante 4");
        }
        sc.close();
    }
}

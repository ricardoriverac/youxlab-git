package Estrutura_Condicional.aula_01;

import java.util.Scanner;


public class exer6 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        double numero;
        System.out.println("Digite um número:");
        numero = sc.nextDouble();

        if (numero <= 25.0) {
            System.out.println("Intervalo (0, 25]");
        }
        else if (numero > 25.0 && numero <= 50.0) {
            System.out.println("Intervalo (25, 50]");
        }
        else if (numero > 50.0 && numero <=75.0) {
            System.out.println("Intervalo (50, 75]");
        }
        else if (numero > 75.0 && numero <= 100.0) {
            System.out.println("Intervalo (75, 100]");
        }
        else {
            System.out.println("Fora de intervalo");
        }
        sc.close();
    }
}

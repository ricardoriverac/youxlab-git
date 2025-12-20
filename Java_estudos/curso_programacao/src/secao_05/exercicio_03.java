package secao_05;

import java.util.Scanner;

public class exercicio_03 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int numero1 = sc.nextInt();
        int numero2 = sc.nextInt();

        if (numero1 > numero2) {
            System.out.println("O primeiro número (" + numero1 + ") é o maior.");
        } else if (numero2 > numero1) {
            System.out.println("O segundo número (" + numero2 + ") é o maior.");
        }
        if (numero1 % numero2 == 0 || numero2 % numero1 == 0) {
            System.out.println("Sao Multiplos");
        }
        else {
            System.out.println("Nao sao Multiplos");
        }

        sc.close();

        }
}


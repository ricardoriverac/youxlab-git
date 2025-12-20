package secao_05;

import java.util.Scanner;

public class exercicio_02 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int numero;
        System.out.println("Digite um numero inteiro");
        numero = sc.nextInt();

        if( numero % 2 == 0) {
            System.out.println("Esse número é par");
        }
        else {
            System.out.println("Esse número é impar");
        }
    }
}

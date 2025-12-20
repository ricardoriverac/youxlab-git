package secao_05;

import java.util.Scanner;

public class exercicio_01 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int numero;
        System.out.println("Digite um numero inteiro");
        numero = sc.nextInt();

        if(numero > 0) {
            System.out.println("Positivo");
        }
        else {
            System.out.println("Negativo");
        }


    }
}

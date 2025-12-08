package secao_04;

import java.util.Scanner;

public class Exercicio_1 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int A, B, soma;
        A = sc.nextInt();
        B = sc.nextInt();

        soma = A+ B;
        System.out.println("Soma = " + soma);
        sc.close();
    }

}

package secao_06;

import java.util.Scanner;

public class exercicio6for {
    static void main() {
        System.out.println("Digite um valor inteiro para ver o seus divisores :");
        Scanner sc = new Scanner(System.in);
        int valor_digitado = sc.nextInt();

        for (int i = 1; i <= valor_digitado; i++) {
            if (valor_digitado % i == 0) {
                System.out.println(i);
            }
            sc.close();
        }
    }
}

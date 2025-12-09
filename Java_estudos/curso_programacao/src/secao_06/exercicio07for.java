package secao_06;

import java.util.Scanner;

public class exercicio07for {
    static void main() {
        System.out.println("Digite um número inteiro: ");
        Scanner sc = new Scanner(System.in);

        int numero_digitado = sc.nextInt();
        for (int i = 1; i<=numero_digitado; i++){
            int primeiro = i;
            int segundo = i * i;
            int terceiro = i * i * i;
            System.out.printf("%d %d %d%n", primeiro, segundo, terceiro);
        }
        sc.close();
    }
}

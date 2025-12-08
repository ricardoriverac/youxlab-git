package secao_5;

import java.util.Scanner;

public class aula_45 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        double preco = 34.5;
        double desconto = (preco < 20.0) ? preco * 0.1 : preco * 0.05;

        System.out.println(desconto);
        sc.close();
    }
}
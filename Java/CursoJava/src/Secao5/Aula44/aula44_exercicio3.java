package Secao5.Aula44;

import java.util.Scanner;

public class aula44_exercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b;
        System.out.print("Digite o primeiro número: ");
        a = sc.nextInt();
        System.out.print("Digite o segundo número: ");
        b = sc.nextInt();
        int maior = Math.max(a, b);
        int menor = Math.min(a, b);
        if (maior  % menor == 0) {
            System.out.println("São multiplos");
        }
        else {
            System.out.println("Não são multiplos");
        }
    }
}

import java.util.Scanner;

public class Exercicio_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n1, n2;

        System.out.print("Digite o 1º número: ");
        n1 = sc.nextInt();

        System.out.print("Digite o 2º número: ");
        n2 = sc.nextInt();

        if (n1 % n2 == 0) {
            System.out.printf("Os números %d e %d são multiplos!!", n1, n2);
        }
        else {
            System.out.printf("Os números %d e %d não são multiplos!!", n1, n2);
        }
    }
}
import java.util.Scanner;

public class Exercicio_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite um número: ");
        int n = sc.nextInt();

        if (n < 0 ){
            System.out.printf("O número %d e negativo", n);
        }
        else {
            System.out.printf("O número %d e positivo", n);
        }

    }
}
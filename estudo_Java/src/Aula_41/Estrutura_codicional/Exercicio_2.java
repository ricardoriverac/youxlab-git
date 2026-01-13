import java.util.Scanner;

public class Exercicio_2 {
    public static void main(String[] args) {
        //n % 2 == 0
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int n = sc.nextInt();

        if (n % 2 == 0){
            System.out.printf("O número %d e PAR!", n);
        }
        else {
            System.out.printf("O número %d e IMPAR!", n);
        }

    }
}
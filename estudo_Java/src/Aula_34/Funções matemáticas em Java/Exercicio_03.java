import java.sql.SQLOutput;
import java.util.Scanner;

public class Exercicio_03 {
    public static void main(String[] args) {

         Scanner sc = new Scanner(System.in);

         int A, B, C, D, resultado;

        System.out.print("Digite o 1º valor: ");
        A = sc.nextInt();

        System.out.print("Digite o 2º valor: ");
        B = sc.nextInt();

        System.out.print("Digite o 3º valor: ");
        C = sc.nextInt();

        System.out.print("Digite o 3º valor: ");
        D = sc.nextInt();

        resultado = (A * B - C * D);
        System.out.printf("A diferença: %d", resultado);



    }
}
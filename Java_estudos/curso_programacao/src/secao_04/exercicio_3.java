package secao_04;
import java.util.Scanner;

public class exercicio_3 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int A, B, C, D, dif;

        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        D = sc.nextInt();

        dif = A * B - C * D;

        System.out.println("DIFERENCA = " + dif);

        sc.close();
    }
}

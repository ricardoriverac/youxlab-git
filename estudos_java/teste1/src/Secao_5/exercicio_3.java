package Secao_5;
import java.util.Scanner;

public class exercicio_3 {
    public static void main(String[] args) {
        int a, b;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();

        if (a%b==0 || b%a==0) {
            System.out.println("These numbers are multiples");
        }
        else {
            System.out.println("These numbers aren't multiples");
        }
    }
}

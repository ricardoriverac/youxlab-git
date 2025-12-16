package Secao_6;
import java.util.Scanner;

public class exercicio_2 {
    public static void main(String[] args) {
        int number;
        Scanner sc = new Scanner (System.in);
        number = sc.nextInt();

        if (number%2==0) {
            System.out.printf("This is a EVEN number");
        }
        else {
            System.out.printf("This is a ODD number");
        }
    }
}

package Secao_10.Exercicio_04;

import java.util.Locale;
import java.util.Scanner;

public class evenNumbers {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many numbers you will enter? ");
        int quantity = sc.nextInt();
        int[] numbers = new int[quantity];

        for (int i=0 ; i<numbers.length ; i++) {
            System.out.print("Enter a number: ");
            numbers[i] = sc.nextInt();
        }

        System.out.println("EVEN NUMBERS:");
        for (int i=0 ; i<numbers.length ; i++) {
            if (numbers[i]%2==0) {
                System.out.printf("%d ",numbers[i]);
            }
        }
    }
}

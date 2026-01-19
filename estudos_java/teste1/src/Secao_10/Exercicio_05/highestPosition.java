package Secao_10.Exercicio_05;

import java.util.Locale;
import java.util.Scanner;

public class highestPosition {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many numbers you will enter? ");
        int quantity = sc.nextInt();
        double[] numbers = new double[quantity];

        double highestNumber = 0.0;
        int highestLocation = 0;

        for (int i=0 ; i<numbers.length ; i++) {
            System.out.print("Enter a number: ");
            double number = sc.nextDouble();
            numbers[i] = number;
            if (number > highestNumber) {
                highestNumber = number;
                highestLocation = i;
            }
        }

        System.out.printf("Highest Value = %.2f%n", highestNumber);
        System.out.printf("Highest Value Position = %d", highestLocation+1);
    }
}

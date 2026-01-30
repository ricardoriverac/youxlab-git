package Secao_10.Exercicio_07;

import java.util.Locale;
import java.util.Scanner;

public class underAverage {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many elements this vect will have? ");
        int quantity = sc.nextInt();
        double[] numbers = new double[quantity];
        double sum = 0.0;

        for (int i=0;i<numbers.length;i++) {
            System.out.print("Enter a number: ");
            numbers[i] = sc.nextInt();
            sum += numbers[i];
        }

        double average = sum/quantity;
        System.out.println("AVERAGE = " + average);
        System.out.println("Values below average:");
        for (int i=0;i<numbers.length;i++) {
            if (numbers[i]<average) {
                System.out.println(numbers[i]);
            }
        }
    }
}

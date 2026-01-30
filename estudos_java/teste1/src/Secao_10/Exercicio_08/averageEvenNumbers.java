package Secao_10.Exercicio_08;

import java.util.Locale;
import java.util.Scanner;

public class averageEvenNumbers {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many numbers will this vect have? ");
        int quantity = sc.nextInt();
        int[] numbers = new int[quantity];
        int evenNumbersSum = 0;
        int evenNumbersQtt = 0;

        for (int i=0 ; i<numbers.length ; i++) {
            System.out.print("Enter a number: ");
            numbers[i] = sc.nextInt();
            if (numbers[i]%2==0) {
                evenNumbersSum += numbers[i];
                evenNumbersQtt += 1;
            }
        }

        if (evenNumbersSum==0) {
            System.out.println("There is no even numbers");
        } else {
            System.out.println("Even numbers average = " + (double)evenNumbersSum/evenNumbersQtt);
        }
    }
}

package Secao_10.Exercicio_02;

import java.util.Locale;
import java.util.Scanner;

public class soma_vetor {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many numbers do you want to enter?");
        int quantity = sc.nextInt();
        double[] vect = new double[quantity];
        double sum = 0.0;

        for ( int i=0 ; i<vect.length ; i++ ) {
            System.out.print("Enter a number: ");
            double number = sc.nextInt();
            vect[i] = number;
            sum += number;
        }
        System.out.printf("Sum = %.2f%n", sum);

        System.out.print("Values = ");
        for (int i = 0; i < vect.length; i++) {
            System.out.print(vect[i]+" ");
        }
        System.out.printf("%nAverage = %f", sum/vect.length);
    }
}

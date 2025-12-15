package Vetores.Parte2.application;

import Vetores.Parte2.entities.ProductVector;

import java.util.Locale;
import java.util.Scanner;

public class Program2 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantidade de produtos: ");
        int prod = sc.nextInt();
        ProductVector[] vect = new ProductVector[prod];

        for (int i=0; i< vect.length; i++) {
            String name = sc.next();
            double price = sc.nextDouble();
            vect[i] = new ProductVector(name, price);
        }

        double sum = 0.0;
        for (int i=0; i< vect.length; i++) {
            sum += vect[i].getPrice();
        }
        double avg = sum / vect.length;
        System.out.printf("AVAREGE PRICE = %.2f", avg);

        sc.close();
    }
}

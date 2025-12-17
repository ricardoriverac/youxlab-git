package curso_completo_java.sessao_10.pratica.exemplo02_pratica.application;


import curso_completo_java.sessao_10.pratica.exemplo02_pratica.etities.Product;

import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Product[] vect = new Product[n];

        for (int i=0; i<n; i++) {
            sc.nextInt();
            String name = sc.nextLine();
            double price = sc.nextDouble();
            vect[i] = new Product(name, price);
        }

        double sum = 0.0;
        for (int i=0; i<vect.length; i++) {
            sum += vect[i].getPrice();
        }
        double avg = sum / vect.length;
        System.out.printf("AVERAGE PRICE = %.2f%n", avg);

    }
}

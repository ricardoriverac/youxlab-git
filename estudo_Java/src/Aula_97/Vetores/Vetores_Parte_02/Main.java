package Aula_97.Vetores.Vetores_Parte_02;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Product[] vect = new Product[n];

        vect[1] = new Product("tv", 12.7);

        for (int i=0; i<n; i++) {
            sc.nextLine();
            String nome = sc.nextLine();
            double preco = sc.nextDouble();
            vect[i] = new Product(nome, preco);

        }


        double sum = 0.0;
        for (int i=0; i<n; i++) {
            sum += vect[i].getPreco();
        }

        double avg = sum / n;

        System.out.printf("AVERDE PRICE = %.2f%n", avg);



    }
}

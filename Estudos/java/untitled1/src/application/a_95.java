package application;

import application.entities.Produto3;

import java.util.Locale;
import java.util.Scanner;

public class a_95 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Produto3[] vect = new Produto3[n];

        for(int i= 0; i<vect.length; i++){
            sc.nextLine();
            String nome = sc.nextLine();
            double preco = sc.nextDouble();
            vect[i] = new Produto3(nome, preco);
        }
        double sum = 0.0;
        for(int i = 0; i< vect.length; i++){
            sum+= vect[i].getPreco();
        }
        double avg = sum/ vect.length;
        System.out.printf("Média de preços: %.2f\n", avg);

        sc.close();
    }
}

package Secao_10.Exercicio_10;

import java.util.Locale;
import java.util.Scanner;

public class approvedStudents {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int quantity = sc.nextInt();
        String[] name = new String[quantity];
        double[] score = new double[quantity];

        for (int i = 0 ; i < name.length ; i++) {
            System.out.println("Enter the name, first and second grade of the first student:");
            sc.nextLine();
            name[i] = sc.nextLine();
            double firstScore = sc.nextDouble();
            double secondScore = sc.nextDouble();
            score[i] = firstScore + secondScore;
        }
        System.out.println("Approved Students:");
        for (int i=0 ; i< score.length ; i++) {
            if (score[i]/2 >= 6.0) {
                System.out.println(name[i]);
            }
        }
    }
}

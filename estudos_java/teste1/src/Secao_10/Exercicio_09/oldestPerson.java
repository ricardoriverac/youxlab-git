package Secao_10.Exercicio_09;

import java.util.Locale;
import java.util.Scanner;

public class oldestPerson {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many people you will enter? ");
        int quantity = sc.nextInt();
        String[] name = new String[quantity];
        int[] age = new int[quantity];
        int oldestAge = 0;
        String oldestName = "";

        for (int i=0 ; i<name.length ; i++) {
            System.out.printf("Data about the %d°person:%n", i+1);
            sc.nextLine();
            System.out.print("Name:");
            name[i] = sc.nextLine();
            System.out.print("Age:");
            age[i] = sc.nextInt();
            if (age[i]>oldestAge) {
                oldestAge = age[i];
                oldestName = name[i];
            }
        }
        System.out.println("The oldest person is: " + oldestName);
    }
}

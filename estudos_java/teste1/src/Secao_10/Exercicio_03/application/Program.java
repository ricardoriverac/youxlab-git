package Secao_10.Exercicio_03.application;

import Secao_10.Exercicio_03.entities.Person;

import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many people will be entered into the registry?");
        int quantity = sc.nextInt();

        String[] name = new String[quantity];
        int[] age = new int[quantity];
        double[] height = new double[quantity];
        int minor = 0;
        double totalHeight = 0.0;

        for (int i=0 ; i<name.length ; i++) {
            sc.nextLine();
            System.out.printf("%d°Person data: %n", i+1);
            System.out.print("Name: ");
            String ownName = sc.nextLine();
            name[i] = ownName;

            System.out.print("Age: ");
            int ownAge = sc.nextInt();
            age[i] = ownAge;
            if (ownAge<16) {
                minor+=1;
            }

            System.out.print("Height: ");
            double ownHeight = sc.nextDouble();
            height[i] = ownHeight;
            totalHeight += ownHeight;
        }

        System.out.println();
        System.out.printf("Average Height %.2f%n", totalHeight/height.length);

        System.out.printf("People below 16 years old: %.1f%s%n", (double)minor/age.length*100, "%");
        for (int i=0 ; i< name.length ; i++) {
            if (age[i]<16) {
                System.out.println(name[i]);
            }
        }
    }
}

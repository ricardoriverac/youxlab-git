package Secao_10.Exercicio_11;

import java.util.Locale;
import java.util.Scanner;

public class peopleData {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter how many people do you want to insert: ");
        int quantity = sc.nextInt();
        double[] height = new double[quantity];
        String[] gender = new String[quantity];

        System.out.print("1°Person height:");
        height[0] = sc.nextDouble();
        double lowest = height[0];
        double highest = height[0];
        System.out.print("1°Person gender:");
        sc.nextLine();
        gender[0] = sc.nextLine();

        for (int i=1 ; i<height.length ; i++) {
            System.out.printf("%d°Person height:", i+1);
            height[i] = sc.nextDouble();
            if (height[i] > highest) {
                highest = height[i];
            }
            if (height[i] < lowest) {
                lowest = height[i];
            }
            System.out.printf("%d°Person gender:", i+1);
            sc.nextLine();
            gender[i] = sc.nextLine();
        }
        System.out.println("Highest = " + highest);
        System.out.println("Lowest = " + lowest);
    }
}

package Secao8.Aula77_ex1;

import java.util.Locale;
import java.util.Scanner;

public class programa {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        retangle Retangle = new retangle();
        System.out.print("Enter rectangle width and height: ");
        Retangle.width = sc.nextDouble();
        Retangle.height = sc.nextDouble();

        System.out.println(Retangle);



        System.out.println();
    }
}

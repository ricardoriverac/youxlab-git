package Secao_8.Exercicio_1.Program;

import java.util.Locale;
import java.util.Scanner;
import Secao_8.Exercicio_1.Rectangle.entities;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        entities rectangle = new entities();
        System.out.println("Enter rectangle width ad height:");
        double width = sc.nextDouble();
        double height = sc.nextDouble();
        rectangle.width = width;
        rectangle.height = height;

        System.out.printf("AREA = %.2f%nPERIMETER = %.2f%nDIAGONAL = %.2f", rectangle.Area(), rectangle.Perimeter(), rectangle.Diagonal());
    }
}

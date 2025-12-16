package Secao_5;

import java.util.Scanner;
import java.util.Locale;

public class exercicio_6 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double a, b, c, triangle, circle, trapeze, square, rectangle;
        System.out.println("Enter the lenght size in cm:");
        a = sc.nextDouble();
        System.out.println("Enter the widht size in cm:");
        b = sc.nextDouble();
        System.out.println("Enter the height size in cm:");
        c = sc.nextDouble();
        triangle = (a*c)/2;
        circle = (Math.pow(c,2)*3.14159);
        trapeze = ((a+b)*c)/2;
        square = Math.pow(b,2);
        rectangle = a*b;

        System.out.printf("TRIANGULE: %.3f%nCÍRCULO: %.3f%nTRAPÉZIO: %.3f%nQUADRADO: %.3f%nRECTANGLE: %.3f%n",triangle,circle,trapeze,square,rectangle);
    }
}

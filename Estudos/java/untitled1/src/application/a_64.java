package application;

import application.entities.Triangle;

import java.util.Locale;
import java.util.Scanner;

public class a_64 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Triangle x, y;
        x = new Triangle();
        y = new Triangle();
        System.out.println("Insira as medidas do triângulo X: ");
        x.a = sc.nextDouble();
        x.b = sc.nextDouble();
        x.c = sc.nextDouble();
        System.out.println("Insira as medidas do triângulo Y: ");
        y.a = sc.nextDouble();
        y.b = sc.nextDouble();
        y.c = sc.nextDouble();


        double areaX = x.area();
        double areaY = y.area();
        System.out.printf("Área do triângulo X: %.4f\n", areaX);
        System.out.printf("Área do triângulo Y: %.4f\n", areaY);

        if (areaX > areaY){
            System.out.print("Maior área: X");
        }
        else{
            System.out.print("Maior área: Y");
        }
        sc.close();

    }
}

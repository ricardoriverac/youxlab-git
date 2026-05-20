package MetodosAbstratos.application;

import MetodosAbstratos.model.entities.Circle;
import MetodosAbstratos.model.entities.Rectangle;
import MetodosAbstratos.model.entities.Shape;
import MetodosAbstratos.model.enums.Color;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class ProgramPrincipal {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of shapes: ");
        int qntShapes = sc.nextInt();
        double area = 0.0;
        List<Shape> shapes = new ArrayList<>();
        for (int i = 0; i < qntShapes; i++) {
            System.out.println("Shape #" + (i + 1) + " data:");
            System.out.print("Rectangle or Circle (r/c)? ");
            char rc = sc.next().toLowerCase().charAt(0);
            System.out.print("Color (BLACK/BLUE/RED): ");
            Color color = Color.valueOf(sc.next().toUpperCase());

            if (rc == 'c') {
                System.out.print("Radius: ");
                double radius = sc.nextDouble();
                shapes.add(new Circle(color, radius));
                area += radius;
            }
            else {
                System.out.print("Width: ");
                double width = sc.nextDouble();
                System.out.print("Height: ");
                double height = sc.nextDouble();
                shapes.add(new Rectangle(color, width, height));
                area += height * width;
            }
        }

        System.out.println();
        System.out.println("SHAPE AREAS:");
        for (Shape s : shapes){
            System.out.println(String.format("%.2f", s.area()));
        }



        sc.close();
    }
}

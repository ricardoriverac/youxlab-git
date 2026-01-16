package curso_completo_java.sessao_13.pratica.exemplo_pratica07.application;

// AULA 144 - Métodos abstrados

import curso_completo_java.sessao_13.pratica.exemplo_pratica07.entities.Circle;
import curso_completo_java.sessao_13.pratica.exemplo_pratica07.entities.Color;
import curso_completo_java.sessao_13.pratica.exemplo_pratica07.entities.Retangle;
import curso_completo_java.sessao_13.pratica.exemplo_pratica07.entities.Shape;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Shape> list = new ArrayList<>();

        System.out.println("Enter the number of shapes: ");
        int n = sc.nextInt();

        for (int i=1; i<=n; i++){
            System.out.println("Shape #" + i + " data:");
            System.out.print("Rectangle or Circle (r/c)?: ");
            char ch = sc.next().charAt(0);
            System.out.print("Color (BLACK/BLUE/RED):");
            Color color = Color.valueOf(sc.next().toUpperCase());
            if (ch == 'r') {
                System.out.print("Width: ");
                double width = sc.nextDouble();
                System.out.print("Height: ");
                double height = sc.nextDouble();
                list.add(new Retangle(color, width, height));
            }
            else {
                System.out.print("Radius: ");
                double radius = sc.nextDouble();
                list.add(new Circle(color, radius));
            }
        }

        System.out.println();
        System.out.println("SHAPE AREAS:");
        for (Shape shape : list) {
            System.out.println(String.format("%.2f", shape.area()));
        }





        sc.close();
    }
}

package curso_completo_java.sessao_17.pratica.exemplo_pratica04.application;

import curso_completo_java.sessao_17.pratica.exemplo_pratica04.entities.Circle;
import curso_completo_java.sessao_17.pratica.exemplo_pratica04.entities.Rectangle;
import curso_completo_java.sessao_17.pratica.exemplo_pratica04.entities.Shape;

import java.util.ArrayList;
import java.util.List;

// AULA 189 - Curingas delimitados / Problema 1

public class program {

    public static void main(String[] args) {

        List<Shape> myShapes = new ArrayList<>();
        myShapes.add(new Rectangle(3.0, 2.0));
        myShapes.add(new Circle(2.0));

        List<Circle> myCircles = new ArrayList<>();
        myCircles.add(new Circle(2.0));
        myCircles.add(new Circle(3.0));

        System.out.println("Total area: " + totalArea(myCircles));
    }

    public static double totalArea(List<? extends Shape> list) {
        double sum = 0.0;
        for (Shape s : list) {
            sum += s.area();
        }
        return sum;
    }
}

package secao_16.aula_180.application;

import secao_16.aula_180.model.entities.AbstractShape;
import secao_16.aula_180.model.entities.Circle;
import secao_16.aula_180.model.entities.Rectangle;
import secao_16.aula_180.model.enums.Color;

public class Program {

        public static void main(String[] args) {

            AbstractShape s1 = new Circle(Color.BLACK, 2.0);
            AbstractShape s2 = new Rectangle(Color.WHITE, 3.0, 4.0);

            System.out.println("Circle color: " + s1.getColor());
            System.out.println("Circle area: " + String.format("%.3f", s1.area()));
            System.out.println("Rectangle color: " + s2.getColor());
            System.out.println("Rectangle area: " + String.format("%.3f", s2.area()));
        }
    }


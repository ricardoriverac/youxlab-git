package curso_completo_java.sessao_16.pratica.exemplo_pratica01.application;

// AULA 180 -   Herdar vs. cumprir contrato

import curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.entities.AbstractShape;
import curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.entities.Circle;
import curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.entities.Rectangle;
import curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.enums.Color;


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

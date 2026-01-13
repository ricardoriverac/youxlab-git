package secao_13.metodosAbstratos.teoria.entities;

import java.awt.*;

public class Circle extends Shape {
    private Double radius;

    public Circle(secao_13.metodosAbstratos.teoria.enums.Color color, double radius) {
        super();
    }

    public Circle(Color color, Double radius) {
        super(color);
        this.radius = radius;
    }

    public Double getRadius() {
        return radius;
    }

    public void setRadius(Double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

package Secao_13.Aula_145.Metodos_abstratos.entities;

import Secao_13.Aula_145.Metodos_abstratos.entities_enum.Color;

public class Circle extends Shape{

    private Double radius;

    public Circle() {
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
        return Math.PI * radius *radius;
    }
}

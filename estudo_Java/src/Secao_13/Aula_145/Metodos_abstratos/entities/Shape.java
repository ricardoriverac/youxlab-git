package Secao_13.Aula_145.Metodos_abstratos.entities;

import Secao_13.Aula_145.Metodos_abstratos.entities_enum.Color;

public abstract class Shape {

    private Color color;

    public Shape() {}

    public Shape(Color color) {
        this.color = color;
    }

    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }

    public abstract double area();
}

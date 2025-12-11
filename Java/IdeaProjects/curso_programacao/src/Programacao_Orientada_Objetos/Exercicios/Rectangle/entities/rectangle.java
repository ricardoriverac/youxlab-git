package Programacao_Orientada_Objetos.Exercicios.Rectangle.entities;

public class rectangle {
    public static double widht;
    public static double height ;

    public static double area() {
        return widht * height;
    }

    public static double perimeter() {
        return (widht + height) * 2;
    }

    public static double diagonal() {
        return Math.sqrt((widht * widht) + (height * height));
    }
}

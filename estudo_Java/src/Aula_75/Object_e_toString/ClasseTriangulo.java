package Aula_75.Object_e_toString.Aula_72;

public class ClasseTriangulo {

    public double a;
    public double b;
    public double c;

    public double area() {
        double p = (a + b + c) / 2.0;
        return Math.sqrt(p * (p - a) * (p - b) * (p - c));
    }
}
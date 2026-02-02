package curso_completo_java.sessao_08.pratica.exercicio01_pratica.entities;

public class Triangle {

    public double a;
    public double b;
    public double c;

    public double area() {
        double p = (a + b + c ) / 2.0;
        return Math.sqrt(p * (p - a) * (p - b) * (p - c));
    }
}

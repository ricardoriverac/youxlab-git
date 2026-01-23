package secao7_introOrientacaoaObjetos.exercicios.exercicio1;

import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

public class metodos1 {
    public double Width;
    public double height;

    public double area() {
        return Width * height;
    }
    public double perimetro() {
        return 2 * (Width + height);
    }
    public double diagonal() {
        return sqrt(pow(Width, 2) + pow(height, 2));
    }
    public String toString(){
        return  "Área = " + area()
                + "\nPerímetro = " + String.format("%.2f", perimetro())
                + "\nDiagonal = " + String.format("%.2f", diagonal())
                ;
    }
}

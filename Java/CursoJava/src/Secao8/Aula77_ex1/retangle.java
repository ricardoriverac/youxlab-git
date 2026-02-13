package Secao8.Aula77_ex1;

public class retangle {
    public double width;
    public double height;

    public double totalArea() {
        return width * height;
    }
    public double totalPerimeter() {

        return 2 * (width + height);
    }
    public double totalDiagonal() {

        return Math.sqrt(Math.pow(width, 2) + Math.pow(height, 2));
    }

    public String toString() {
        return "Area = "
                + String.format("%.2f\n", totalArea())
                +"Perimeter = "
                + String.format("%.2f\n", totalPerimeter())
                +"Diagonal = "
                + String.format("%.2f", totalDiagonal());
    }
}

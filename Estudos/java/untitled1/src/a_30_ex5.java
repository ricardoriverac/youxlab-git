import java.util.Scanner;
import java.util.Locale;
public class a_30_ex5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        double a, b, c, triangulo, areaCirculo, areaTrapezio, areaQuadrado, areaRetangulo;
        System.out.print("Digite o valor de A: ");
        a = sc.nextDouble();
        System.out.print("Digite o valor de B: ");
        b = sc.nextDouble();
        System.out.print("Digite o valor de C: ");
        c = sc.nextDouble();
        triangulo = (a * c) / 2;
        System.out.printf("Considerando %f como base do triângulo e %f como altura do triângulo, a área do triângulo é %f \n", a, c, triangulo);
        areaCirculo = 3.14159 * (Math.pow(c, 2));
        System.out.printf("Considerando %f como raio do círculo, a área do círculo é %f \n", c, areaCirculo);
        areaTrapezio = (a + b) * c/2;
        System.out.printf("Considerando %f e %f como base do Trapezio e também %f como altura, a área do trapezio é %f \n", a, b, c, areaTrapezio);
        areaQuadrado = Math.pow(b , 2);
        System.out.printf("Considerando %f como lado do quadrado, a área do quadrado é %f \n", b, areaQuadrado);
        areaRetangulo = a * b;
        System.out.printf("Considerando %f e %f como lados do retângulo, a área do quadrado é %f \n", a, b, areaRetangulo);
        Locale.setDefault(Locale.US);
    }
}

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_06 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        //Variaveis
        double valorA, valorB, valorC, triangulo, circulo, trapezio, quadrado, retangulo, pi = 3.14159;

        // Receptor do valor A
        System.out.print("Digite o 1º valor: ");
        valorA = sc.nextDouble();

        // Receptor do valor B
        System.out.print("Digite o 2º valor: ");
        valorB = sc.nextDouble();

        // Receptor do valor C
        System.out.print("Digite o 3º valor: ");
        valorC = sc.nextDouble();

        //Resultado
        triangulo = (valorA * valorC) / 2;
        circulo =  (Math.pow(valorC, 2) * pi);
        trapezio = (valorA+ valorB) * valorC / 2;
        quadrado = Math.pow(valorB, 2);
        retangulo = valorA * valorB;

        System.out.printf("TRIÂNGULO: %.3f %n", triangulo);
        System.out.printf("CIRCULO: %.3f %n", circulo);
        System.out.printf("TRAPEZIO: %.3f %n", trapezio);
        System.out.printf("QUADRADO: %.3f %n", quadrado);
        System.out.printf("RETANGULO: %.3f %n", retangulo);

    }
}
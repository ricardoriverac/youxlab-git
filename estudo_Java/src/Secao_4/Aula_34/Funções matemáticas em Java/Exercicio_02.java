import java.util.Locale;
import java.util.Scanner;

public class Exercicio_02 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);

        double raio, pi = 3.14159, resultado;

        System.out.print("Digite o valor do raio: ");
        raio = sc.nextDouble();

        resultado = pi *  (Math.pow(raio,2));
        System.out.printf("O resultado da area = %.4f", resultado);

        sc.close();


        
    }
}

package secao_5;
import java.util.Scanner;

public class exercicio_05 {
    static void main() {

        Scanner sc = new Scanner(System.in);
        double numero = sc.nextDouble();

        if (numero < 0.0 && numero > 100.0) {
            System.out.println("Fora de intervalo");
        }
        else if (numero <= 25.0) {
            System.out.println("Intervalo de [0, 25]");
        }
        else if (numero > 25.0 && numero <= 50.0) {
            System.out.println("intervalo de (25,50]");

        } else if (numero > 50.0 && numero <= 75.0) {
            System.out.println("intervalo de (50,75]");

        } else if (numero > 75.0 && numero <= 100.0) {
            System.out.println("Intervalo de (75,100]");

        }
    sc.close();

    }
}

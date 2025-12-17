package curso_completo_java.sessao_06.pratica;

import java.util.Locale;
import java.util.Scanner;

public class pratica_exemplo04 {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            char resposta;
            do {
                System.out.print("Digite a temperatura em Celsius: ");
                double Celsius = sc.nextDouble();

                double Fahrenheit = 9.0 * Celsius / 5.0 + 32.0;
                System.out.printf("Equivalente em Fahrenheit: %.1f%n", Fahrenheit);

                System.out.print("Deseja repetir (s/n)? ");
                resposta = sc.next().charAt(0);

            } while (resposta != 'n');
            System.out.println("Encerrado!");
            sc.close();
        }
    }

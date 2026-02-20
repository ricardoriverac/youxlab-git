import java.util.Locale;
import java.util.Scanner;

public class Exercicio_7 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a 1º coordenada: ");
        double Coordenadax = sc.nextDouble();

        System.out.print("Digite a 2º coordenada: ");
        double Coordenaday = sc.nextDouble();

        if (Coordenadax > 0 && Coordenaday > 0){
            System.out.println("Q1");
        }
        else if (Coordenadax < 0 && Coordenaday > 0){
            System.out.println("Q2");
        }
        else if (Coordenadax < 0 && Coordenaday < 0) {
            System.out.println("Q3");
        }
        else if (Coordenadax > 0 && Coordenaday < 0){
            System.out.println("Q4");
        }
        else if (Coordenadax == 0 && Coordenaday == 0) {
            System.out.println("Origem");
        }
    }
}
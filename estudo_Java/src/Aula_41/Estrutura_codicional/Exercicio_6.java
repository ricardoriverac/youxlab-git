import java.util.Locale;
import java.util.Scanner;

public class Exercicio_6 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um númerico: ");
        double Receptor_numerico = sc.nextDouble();

        if (Receptor_numerico < 0 || Receptor_numerico > 100){
            System.out.println("Fora do intervalo.");
        }
        else if (25 >= Receptor_numerico) {
            System.out.println("Intervalo (0, 25)");
        }
        else if (50 >= Receptor_numerico) {
            System.out.println("Intervalo (25, 50)");
        }
        else if (75 >= Receptor_numerico) {
            System.out.println("Intervalo (50, 75)");
        }
        else if (100 <= Receptor_numerico) {
            System.out.println("Intervalo (75, 100)");
        }
    }
}
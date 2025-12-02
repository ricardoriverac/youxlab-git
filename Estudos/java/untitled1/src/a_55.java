import java.util.Scanner;
import java.util.Locale;

public class a_55 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        char resp;

        do {
            System.out.print("Caro usuário, por favor digite quantos celsius está hoje: ");
            double celsius = sc.nextDouble();
            double fahrenheit = (celsius * 1.80 + 32);
            System.out.printf("Caro usuário, está %.2f fahrenheit\n", fahrenheit);
            System.out.print("Caro cliente, deseja continuar? [s/n]");
            resp = sc.next().charAt(0);
        }
         while (resp != 'n');
        sc.close();
    }
}

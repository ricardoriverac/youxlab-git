import java.util.Scanner;
import java.util.Locale;

public class a_55 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, por favor digite quantos celsius está hoje: ");
        double celsius = sc.nextDouble();
        double fahrenheit = (celsius * 1.80 + 32);
        System.out.printf("Caro usuário, está %.2f fahrenheit\n", fahrenheit);
        System.out.print("Caro cliente, deseja continuar? [s/n]");
        char resp = sc.next().charAt(0);

        while (resp != 'n'){
            System.out.print("Caro usuário, por favor digite quantos celsius está hoje: ");
            celsius = sc.nextDouble();
            fahrenheit = (celsius * 1.80 + 32);
            System.out.printf("Caro usuário, está %.2f fahrenheit", fahrenheit);
            resp = sc.next().charAt(0);

        }
        sc.close();
    }
}

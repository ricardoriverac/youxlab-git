import java.util.Locale;
import java.util.Scanner;

public class a_38 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        System.out.print("Caro usuário, por favor insira quantos minutos você passou em ligação: ");
        int minuto = sc.nextInt();
        double conta;
        conta = 50.0;

        if (minuto > 100) {
            conta += (minuto-100) * 2.0;
        }
        System.out.printf("Valor da conta = %.2f\n", conta);

        sc.close();
    }
}

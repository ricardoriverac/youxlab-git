import java.util.Scanner;
import java.util.Locale;
public class a_37_ex5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        int codigo, quantidade;
        double valorFinal;
        System.out.print("Caro usuário, digite o código do produto comprado: ");
        codigo = sc.nextInt();
        System.out.print("Caro usuário, por favor digite a quantidade de unidades compradas do produto: ");
        quantidade = sc.nextInt();

        if (codigo == 1) {
            valorFinal = 4 * quantidade;
            System.out.printf("Caro usuário, comprando %d unidades do produto o valor à ser pago será %.2f ", quantidade, valorFinal);

        }
        if (codigo ==2) {
            valorFinal = 4.50f * quantidade;
            System.out.printf("Caro usuário, comprando %d unidades do produto o valor à ser pago será %.2f", quantidade, valorFinal);

        }
        if (codigo == 3) {
            valorFinal = 5.0f * quantidade;
            System.out.printf("Caro usuário, comprando %d unidades do produto o valor à ser pago será %.2f", quantidade, valorFinal);

        }
        if (codigo == 4) {
            valorFinal = 2.0f * quantidade;
            System.out.printf("Caro usuário, comprando %d unidades do produto o valor à ser pago será %.2f", quantidade, valorFinal);
        }
        if (codigo == 5) {
            valorFinal = 1.50f * quantidade;
            System.out.printf("Caro usuário, comprando %d unidades do produto o valor à ser pago será %.2f", quantidade, valorFinal);
        }
        sc.close();
    }
}

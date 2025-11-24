
import java.util.Scanner;
public class a_37_ex2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numero;

        System.out.print("Caro usuário, por favor insira o valor desejado: ");
        numero = sc.nextInt();

        if (numero % 2 == 0) {
            System.out.printf("O número %d é par!", numero);
        }
        else{
            System.out.printf("O número %d é ímpar!", numero);
        }
        sc.close();
    }
}

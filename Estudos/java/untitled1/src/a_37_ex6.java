import java.util.Scanner;
import  java.util.Locale;
public class a_37_ex6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        double valor;

        System.out.print("Caro usuário, por favor digite o valor desejado: ");
        valor = sc.nextDouble();

        if (0 > valor || valor > 100) {
            System.out.print("Intervalo inválido!");
        }
        else if (valor <= 25){
            System.out.printf("O valor %.2f está no intervalo de [0, 25]", valor);
        }
        else if (valor <= 50) {
            System.out.printf("O número %.2f está no intervalo de [25, 50]", valor);
        }
        else{
            System.out.printf("O número %.2f está no intervalo de [75,100]", valor);
        }
    }
}

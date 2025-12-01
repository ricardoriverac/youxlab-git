import java.util.Scanner;
import java.util.Locale;
public class a_54_ex3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        int limiteTeste;
        System.out.print("Caro usuário, por favor insira quantos testes você deseja fazer?");
        limiteTeste= sc.nextInt();

        for (int i = 0; i < limiteTeste; i++) {
            float primeiroValor, segundoValor, terceiroValor;
            int peso = 2+3+5;
            float valores, mediaPonderada;
            System.out.print("Caro usuãrio, por favor insira o valor que você deseja para o primeiro valor: ");
            primeiroValor = sc.nextFloat();

            System.out.print("Caro usuário, por favor insira o valor que você deseja para o segundo valor: ");
            segundoValor = sc.nextFloat();

            System.out.print("Caro usuário, por favor insira o valor que você deseja para o terceiro valor: ");
            terceiroValor = sc.nextFloat();

            valores = (primeiroValor * 2) + (segundoValor * 3) + (terceiroValor * 5);
            mediaPonderada = valores/ 10;
            System.out.printf("Caro cliente, a média ponderada deste cálculo é %.2f\n", mediaPonderada);
        }

    }
}

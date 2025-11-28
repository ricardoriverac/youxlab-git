import java.util.Scanner;
import java.util.Locale;

public class a_55_ex4 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int limitePares;
        System.out.print("Caro usuário, por favor insira quantos pares você deseja calcular");
        limitePares = sc.nextInt();

        for (int i = 0; i < limitePares; i++) {
            int valor1,valor2;
            double divisao;

            System.out.print("Caro usuário, por favor insira o primeiro valor do par numérico à ser verificado: ");
            valor1 = sc.nextInt();
            System.out.print("Caro usuário, por favor insira o segundo valor do par numérico à ser verificado: ");
            valor2 = sc.nextInt();
            divisao = valor1/valor2;
             if (divisao <= 0){
                 System.out.print("Divisão impossível\n");
             }
             else {
                 System.out.printf("Resultado: %.2f\n", divisao);
             }

        }
    }
}

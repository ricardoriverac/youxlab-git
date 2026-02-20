import java.util.Scanner;

public class Exercicio_01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int valor1, valor2, resultado;

        System.out.print("Digite o 1º número: ");
        valor1 = sc.nextInt();

        System.out.print("Digite o 2º número: ");
        valor2 = sc.nextInt();

        resultado = (valor1 + valor2);

        System.out.printf("A soma de %d e %d = %d", valor1, valor2, resultado);

        sc.close();


    }
}

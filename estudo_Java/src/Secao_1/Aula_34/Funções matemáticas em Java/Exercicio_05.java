import java.util.Scanner;

public class Exercicio_05 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int codigo_peca1, numeros_pecas1;
        int codigo_peca2, numeros_pecas2;
        double valor_unitario1, valor_unitario2, resultado;

        System.out.print("Digite o codígo da 1º peça: ");
        codigo_peca1 = sc.nextInt();

        System.out.print("Digite o número da 1º peça: ");
        numeros_pecas1 = sc.nextInt();

        System.out.print("Digite o valor da 1º peça: ");
        valor_unitario1 = sc.nextDouble();

        System.out.print("Digite o codígo da 2º peça: ");
        codigo_peca2 = sc.nextInt();

        System.out.print("Digite o número da 2º peça: ");
        numeros_pecas2 = sc.nextInt();

        System.out.print("Digite o valor da 2º peça: ");
        valor_unitario2 = sc.nextDouble();

        resultado = (valor_unitario2 * numeros_pecas2) + (valor_unitario1 * numeros_pecas1);

        System.out.printf("Valor a pagar %.2f", resultado);



    }
}
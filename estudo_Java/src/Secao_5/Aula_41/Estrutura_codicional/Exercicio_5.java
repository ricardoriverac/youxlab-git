import java.util.Scanner;

public class Exercicio_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double Quantidade_item, Codigo_item, resultado;
        double Cachorro_quente = 4.00, x_salada = 4.50, x_bacon = 5.00, Torrada_simples = 2.00, Refrigerante = 1.50;

        System.out.println("----------------------------------------------");
        System.out.println("CODIGO | ESPECIFICACAO       | PRECO");
        System.out.println("----------------------------------------------");
        System.out.println("1      | Cachorro Quente    | R$ 4.00");
        System.out.println("2      | X-Salada           | R$ 4.50");
        System.out.println("3      | X-Bacon            | R$ 5.00");
        System.out.println("4      | Torrada simples    | R$ 2.00");
        System.out.println("5      | Refrigerante       | R$ 1.50");
        System.out.println("----------------------------------------------");

        System.out.print("Digite o código do item: ");
        Codigo_item = sc.nextDouble();

        System.out.print("Digite o preço do item: ");
        Quantidade_item = sc.nextDouble();

        if (Quantidade_item > 5) {
            System.out.println("Esse item não existe!!");
        }
        else if (Codigo_item == 1) {
            resultado = Quantidade_item * Cachorro_quente;
            System.out.printf("O valor total é R$%.2f", resultado);
        }
        else if (Codigo_item == 2) {
            resultado = Quantidade_item * x_salada;
            System.out.printf("O valor total é R$%.2f", resultado);
        }
        else if (Codigo_item == 3) {
            resultado = Quantidade_item * x_bacon;
            System.out.printf("O valor total é R$%.2f", resultado);
        }
        else if (Codigo_item == 4) {
            resultado = Quantidade_item * Torrada_simples;
            System.out.printf("O valor total é R$%.2f", resultado);
        }
        else {
            resultado = Quantidade_item * Refrigerante;
            System.out.printf("O valor total é R$%.2f", resultado);
        }
    }
}
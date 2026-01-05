package secao5_estrutura_condicional.exercicios_elif;

import java.util.Scanner;

public class exercicio5 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o ID do produto:");
        int idProduto = sc.nextInt();
        System.out.println("Digite a quantidade do produto:");
        int quantidade = sc.nextInt();
        double total;
        if (idProduto == 1) {
            total = quantidade * 4;
            System.out.printf("Total: R$ %.2f%n", total);
        }
        else if (idProduto == 2) {
            total = quantidade * 4.50;
            System.out.printf("Total: R$ %.2f%n", total);
        }
        else if (idProduto == 3) {
            total = quantidade * 5;
            System.out.printf("Total: R$ %.2f%n", total);
        }
        else if (idProduto == 4) {
            total = quantidade * 2;
            System.out.printf("Total: R$ %.2f%n", total);
        }
        else if (idProduto == 5) {
            total = quantidade * 1.5;
            System.out.printf("Total: R$ %.2f%n", total);

        }
    }

}

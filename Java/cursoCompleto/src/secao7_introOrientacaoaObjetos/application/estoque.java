package secao7_introOrientacaoaObjetos.application;

import java.util.Locale;
import java.util.Scanner;

import secao7_introOrientacaoaObjetos.entities.produto;

public class estoque {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        produto produto = new produto();

        System.out.println("ENTER PRODUCT DATA:");
        System.out.print("NAME: ");
        produto.nome = sc.next();
        System.out.print("PRICE: ");
        produto.preco = sc.nextDouble();
        System.out.print("QUANTITY IN STOCK: ");
        produto.quantidade = sc.nextInt();
        System.out.println("UPDATED DATA: " + produto);
        System.out.print("\nENTER THE NUMBER OF PRODUCTS TO BE ADDED IN STOCK: ");
        int quantidade = sc.nextInt();
        produto.addProdutos(quantidade);

        System.out.println("UPDATED DATA: " + produto);

        System.out.print("\nENTER THE NUMBER OF PRODUCTS TO BE REMOVED IN STOCK: ");
        quantidade = sc.nextInt();
        produto.removerProdutos(quantidade);

        System.out.println("UPDATED DATA: " + produto);
        sc.close();
    }
}

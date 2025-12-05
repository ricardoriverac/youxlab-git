package application;
import java.util.Locale;
import java.util.Scanner;

import application.entities.Produto2;
import cursor.entities.Produto;

public class a_81 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        String nome = sc.nextLine();
        System.out.print("Price: ");
        double preco = sc.nextDouble();
        System.out.print("Quantity in stock: ");
        int quantidade = sc.nextInt();
        Produto2 product = new Produto2(nome, preco, quantidade);
        System.out.println();
        System.out.println("Product data: " + product);
        System.out.println();
        System.out.print("Enter the number of products to be added in stock: ");
        int quantity = sc.nextInt();
        product.adicionarEstoque(quantity);
        System.out.println();
        System.out.println("Updated data: " + product);
        System.out.println();
        System.out.print("Enter the number of products to be removed from stock: ");
        quantity = sc.nextInt();
        product.removerEstoque(quantity);
        System.out.println();
        System.out.println("Updated data: " + product);
        sc.close();
    }
}


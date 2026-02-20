package Aula_75.Object_e_toString;

import java.util.Locale;
import java.util.Scanner;

public class CodigoProduto {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        ClasseProduto prd = new ClasseProduto();

        System.out.println("Inserir dados do produto: ");
        System.out.print("Nome: ");
        prd.name = sc.nextLine();
        System.out.print("Produto: ");
        prd.price = sc.nextDouble();
        System.out.print("Quantidade em estoque: ");
        prd.quantity = sc.nextInt();

        System.out.println();
        System.out.println("Product data: " + prd);

        System.out.println();
        System.out.print("Enter the number of products to be added in stock: ");
        int quantity = sc.nextInt();
        prd.addProducts (quantity);

        System.out.println();
        System.out.println("Updated data: " + prd);

        System.out.println();
        System.out.print("Enter the number of products to be removed from stock: ");
        quantity = sc.nextInt();
        prd.removeProducts (quantity);

        System.out.println();
        System.out.println("Updated data: " + prd);

        sc.close();

    }
}
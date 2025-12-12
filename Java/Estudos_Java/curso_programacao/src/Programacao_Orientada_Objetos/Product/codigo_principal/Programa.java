package Programacao_Orientada_Objetos.Product.codigo_principal;

import Programacao_Orientada_Objetos.Product.entities.Product;

import java.util.Locale;
import java.util.Scanner;

public class Programa {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Product Product = new Product();
        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        Product.name = sc.nextLine();

        System.out.print("Price: ");
        Product.price = sc.nextDouble();

        System.out.print("Quantity in stock: ");
        Product.quantity = sc.nextInt();

        System.out.println();
        System.out.println("Products data: " + Product);

        System.out.println();
        System.out.print("Enter the number of products to be added in stock: ");
        int quantity = sc.nextInt();
        Product.addProducts(quantity);

        System.out.println();
        System.out.println("Update data: " + Product);

        System.out.println();
        System.out.print("Enter the number of products to be removed from stock: ");
        quantity = sc.nextInt();
        Product.removeProducts(quantity);

        System.out.println();
        System.out.println("Update data: " + Product);

        sc.close();
    }
}

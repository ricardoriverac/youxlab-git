package Secao9.Aula85.entities_melhoria;

import java.util.Locale;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        product p = new product();

        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        String name = sc.nextLine();
        System.out.print("Price: ");
        double price = sc.nextDouble();

        product Product = new product(name, price);

        System.out.println();
        System.out.println("Product data: "+ Product);

        System.out.println();
        System.out.print("Enter the number of products to be added in stock: ");
        int quantity = sc.nextInt();
        Product.addProducts(quantity);

        System.out.println();
        System.out.println("Updated data: "+ Product);

        System.out.println();
        System.out.print("Enter the number of products to be removed from stock: ");
        quantity = sc.nextInt();
        Product.removeProducts(quantity);

        System.out.println();
        System.out.println("Update data: "+ Product);
        sc.close();
    }
}

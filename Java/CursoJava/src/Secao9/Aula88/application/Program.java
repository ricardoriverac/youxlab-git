package Secao9.Aula88.application;

import Secao9.Aula88.entities.Product;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Product product = new Product();
        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        String name = sc.nextLine();
        System.out.print("Price: ");
        double price = sc.nextDouble();

        Product Product = new Product(name, price);

        System.out.println();
        System.out.println("Updated name: "+ Product.getName());
        Product.setPrice(1200.00);
        System.out.println("Updated price: "+ Product.getPrice());

        System.out.println();
        System.out.println("Product data: "+ Product);

        System.out.println();
        System.out.print("Enter the number of products to be added in stock: ");
        int quantity = sc.nextInt();
        product.addProducts(quantity);

        System.out.println();
        System.out.println("Updated data: "+ Product);

        System.out.println();
        System.out.print("Enter the number of products to be removed from stock: ");
        quantity = sc.nextInt();
        product.removeProducts(quantity);

        System.out.println();
        System.out.println("Update data: "+ Product);
        sc.close();
    }
}




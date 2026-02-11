package Secao8.Aula74_pt1.application;

import Secao8.Aula74_pt2.entities.product;

import java.util.Locale;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        product Product = new product();
        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        Product.name = sc.nextLine();
        System.out.print("Price: ");
        Product.price = sc.nextDouble();
        System.out.print("Quantity in stock: ");
        Product.quantity = sc.nextInt();

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

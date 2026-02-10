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

        System.out.println(Product.name + ", " + Product.price + ", " + Product.quantity);
    sc.close();
    }
}

package Secao_9.application;
import java.util.Locale;
import java.util.Scanner;
import Secao_9.entities.Product;
public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        String name = sc.nextLine();
        System.out.print("Price: ");
        double price = sc.nextDouble();
        Product product = new Product(name, price);

        product.setName("Computer");
        System.out.println("Updated name: ");

        Product p = new Product();
        System.out.println();
        System.out.println("Product data: " + product);

        System.out.println();
        System.out.print("Enter the number of products to be added in stock: ");
        int newQuantity = sc.nextInt();
        product.addProducts(newQuantity);
        System.out.println();
        System.out.println("Updated data: " + product);
        System.out.println();
        System.out.print("Enter the number of products to be removed from stock: ");
        newQuantity = sc.nextInt();
        product.removeProducts(newQuantity);
        System.out.println();
        System.out.println("Updated data: " + product);
        sc.close();
    }
}


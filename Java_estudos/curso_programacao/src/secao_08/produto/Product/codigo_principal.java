package secao_08.produto.Product;

import java.util.Locale;
import java.util.Scanner;

public class codigo_principal {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        entities product = new entities();
        System.out.println("Enter product data: ");
        System.out.print("Name: ");
        product.name = sc.nextLine();
        System.out.print("Price: ");
        product.price = sc.nextDouble();
        System.out.print("Quantity in stock: ");
        product.quantity = sc.nextInt();
        System.out.println(product.name + ","  + product.price + "," + product.quantity);




        sc.close();
    }
}

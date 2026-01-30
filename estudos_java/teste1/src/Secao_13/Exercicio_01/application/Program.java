package Secao_13.Exercicio_01.application;

import Secao_13.Exercicio_01.entities.ImportedProduct;
import Secao_13.Exercicio_01.entities.Product;
import Secao_13.Exercicio_01.entities.UsedProduct;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Program {

    public static void main(String[] args) throws ParseException {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Product> list = new ArrayList<>();
        System.out.print("Enter the number of products: ");
        int quantity = sc.nextInt();

        for (int i = 0 ; i < quantity ; i++) {
            sc.nextLine();
            System.out.printf("Product #%d data:%n", i+1);
            System.out.print("Common, used or imported (c/u/i)?: ");
            char ch = sc.nextLine().charAt(0);
            System.out.print("Name: ");
            String name = sc.nextLine();
            System.out.print("Price: ");
            double price = sc.nextDouble();
            if (ch == 'u') {
                System.out.print("Manufacture date (DD/MM/YYYY): ");
                Date date = sdf.parse(sc.next());
                Product product = new UsedProduct(name, price, date);
                list.add(product);
            } else if (ch == 'i') {
                System.out.print("Custom fee: ");
                double customFee = sc.nextDouble();
                Product product = new ImportedProduct(name, price, customFee);
                list.add(product);
            } else {
                Product product = new Product(name, price);
                list.add(product);
            }
        }
        System.out.println();
        System.out.println("PRICE TAGS:");
        for (Product product : list) {
            System.out.print(product.priceTag());
        }

    }

}

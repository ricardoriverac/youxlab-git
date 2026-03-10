package Secao_13.Aula_143.Exercicio_Fixacao.application;

import Secao_13.Aula_143.Exercicio_Fixacao.entities.ImportedProduct;
import Secao_13.Aula_143.Exercicio_Fixacao.entities.Product;
import Secao_13.Aula_143.Exercicio_Fixacao.entities.UsedProduct;

import java.text.SimpleDateFormat;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<Product> productList = new ArrayList<>();
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.print("Enter the number of products: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.printf("\nProduct #%d data: %n", (i+1));

            System.out.print("Common, used or imported (c/u/i)? ");
            char ch = sc.next().charAt(0);

            sc.nextLine();
            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Price: ");
            double price = sc.nextDouble();

            if (ch == 'i') {
                System.out.print("Customs fee: ");
                double customsFee = sc.nextDouble();
                productList.add(new ImportedProduct(name, price, customsFee));
            }
            else if (ch == 'u') {
                System.out.print("Manufacture date (DD/MM/YYYY): ");
                Date manufactureDate = sdf.parse(sc.next());
                productList.add(new UsedProduct(name, price, manufactureDate));
            }
            else if (ch == 'c'){
                productList.add(new Product(name,price));
            }
        }

        System.out.println("\nPRICE TAGS: ");
        for (Product product : productList) {
            System.out.println(product.priceTag());
        }
    }
}

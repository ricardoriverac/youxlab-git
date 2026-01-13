package secao_13.exercicioA142.application142;

import secao_13.exercicioA142.entities142.ImportedProduct;
import secao_13.exercicioA142.entities142.Product;
import secao_13.exercicioA142.entities142.UsedProduct;

import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class SistemaDeProdutos {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<Product> list = new ArrayList<>();

        Product product = new Product();

        System.out.print("Enter the number of products: ");
        int numberProduct = sc.nextInt();

        for (int i=1; i<=numberProduct; i++) {
            System.out.println("Datos do produto #" + i + ":");
            System.out.print("Comum, usado, importado (c/u/i)? ");
            char type = sc.next().charAt(0);
            System.out.print("Nome: ");
            sc.nextLine();
            String name = sc.nextLine();
            System.out.print("Preco: ");
            double price = sc.nextDouble();
            if (type == 'c') {
                list.add(new Product(name, price));
            }
            else if (type == 'u') {
                System.out.print("Data de fabricacao (DD/MM/YYYY): ");
                LocalDate date = LocalDate.parse(sc.next(), DateTimeFormatter.ofPattern("dd/MM/yyyy"));
                list.add(new UsedProduct(name, price, date));
            }
            else {
                System.out.print("Taxa de importacao: ");
                double customsFee = sc.nextDouble();
                list.add(new ImportedProduct(name, price, customsFee));
            }
        }

        System.out.println();
        System.out.println("ETIQUETAS DE PRECO:");
        for (Product prod : list) {
            System.out.println(prod.priceTag());
        }

        sc.close();
    }



}


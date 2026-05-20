package herancaPolimorfismo.Exercicios.ExerciciosFixacao.exer01.application;

import herancaPolimorfismo.Exercicios.ExerciciosFixacao.exer01.entities.ImportedProduct;
import herancaPolimorfismo.Exercicios.ExerciciosFixacao.exer01.entities.Product;
import herancaPolimorfismo.Exercicios.ExerciciosFixacao.exer01.entities.UsedProduct;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class ProgramPrincipal {
    static void main() throws ParseException {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        ImportedProduct imp = new ImportedProduct();
        UsedProduct up = new UsedProduct();

        System.out.print("Enter the number od products? ");
        int numberProducts = sc.nextInt();

        List<Product> products = new ArrayList<>();
        for (int i = 0; i < numberProducts; i++) {
            System.out.println("Product #" + (i+1) + " data:");
            System.out.print("Common, used or imported (c/u/i)? ");
            char cui = sc.next().toLowerCase().charAt(0);
            System.out.print("Name: ");
            sc.nextLine();
            String nameProduct = sc.nextLine();
            System.out.print("Price: ");
            double price = sc.nextDouble();
            if (cui == 'c'){
                products.add(new Product(nameProduct, price));
            }

            else if (cui == 'i'){
                System.out.print("Customs fee: ");
                double customsFee = sc.nextDouble();
                products.add(new ImportedProduct(nameProduct, price, customsFee));
            }
            else if (cui == 'u') {
                System.out.print("Manufacture date: ");
                Date manufacture = sdf.parse(sc.next());
                products.add(new UsedProduct(nameProduct, price, manufacture));
            }
        }

        System.out.println();
        System.out.println("PRICE TAGS:");
        for (Product p : products){
            System.out.println(p.priceTag());
        }




        sc.close();
    }
}

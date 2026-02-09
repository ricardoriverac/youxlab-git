package secao13_Heranca.exercicioProposto1.aplicacao;

import secao13_Heranca.exercicioProposto1.entities.ImportProduct;
import secao13_Heranca.exercicioProposto1.entities.Product;
import secao13_Heranca.exercicioProposto1.entities.UsedProduct;
import secao8_Java.application.Program;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

public class program {
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("dd/MM/yyyy");
        Date date = new Date();
        Scanner sc = new Scanner(System.in);
        List<Product> products = new ArrayList<>();
        System.out.print("Enter the number of products: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++){
            System.out.print("Common, used or imported (c/u/i)? ");
            char condi = sc.next().toLowerCase().charAt(0);
            System.out.print("\nName:");
            String name = sc.next();
            System.out.print("\nPrice: ");
            Double preco = sc.nextDouble();
            if (condi == 'i'){
                System.out.print("Custom fee: ");
                double precoImport = sc.nextDouble();
                products.add(new ImportProduct(name, preco, precoImport));
            }
            else if(condi == 'c'){
                products.add(new Product(name, preco ));
            }
            else {
                System.out.print("Manufactured data: ");
                Date manufecturedData = simpleDateFormat.parse(sc.next());
                products.add((new UsedProduct(name, preco, manufecturedData)));
            }
        }
        for(Product product : products){
            System.out.print(product.priceTag());
        }
    }
}

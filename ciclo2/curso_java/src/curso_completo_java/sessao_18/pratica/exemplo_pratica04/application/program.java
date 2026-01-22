package curso_completo_java.sessao_18.pratica.exemplo_pratica04.application;

import curso_completo_java.sessao_18.pratica.exemplo_pratica04.entities.Product;
import curso_completo_java.sessao_18.pratica.exemplo_pratica04.util.PriceUpdate;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.function.Consumer;

public class program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        List<Product> list = new ArrayList<>();

        list.add(new Product("Tv", 900.00));
        list.add(new Product("Mouse", 50.00));
        list.add(new Product("Tablet", 350.50));
        list.add(new Product("HD Case", 80.90));


        /* Implementação da interface
        list.forEach(new PriceUpdate());
        list.forEach(System.out::println);            */

        /* Reference method com método estático
        list.forEach (Product::staticPriceUpdate);
        list.forEach(System.out::println);            */


        /* Reference method com método não estático
        list.forEach (Product::nonStaticPriceUpdate);
        list.forEach(System.out::println);                */

        /* Expressão lambda declarada
        double factor = 1.1;

        Consumer<Product> cons = p -> {
            p.setPrice(p.getPrice() * factor);
        };

        list.forEach(cons);
        list.forEach(System.out::println);            */

        /*  Expressão lambda inline
        double factor = 1.1;
        list.forEach(p-> p.setPrice(p.getPrice() * factor));
        list.forEach(System.out::println);           */


    }
}


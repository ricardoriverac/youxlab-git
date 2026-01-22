package curso_completo_java.sessao_18.pratica.exemplo_pratica03.application;

import curso_completo_java.sessao_18.pratica.exemplo_pratica03.entities.Product;
import curso_completo_java.sessao_18.pratica.exemplo_pratica03.util.ProductPredicate;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.function.Predicate;

public class program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        List<Product> list = new ArrayList<>();

        list.add(new Product("Tv", 900.00));
        list.add(new Product("Mouse", 50.00));
        list.add(new Product("Tablet", 350.50));
        list.add(new Product("HD Case", 80.90));

        /*  Implementação da interface
        list.removeIf (new ProductPredicate());          */

        /* Reference method com método estático
        list.removeIf (Product :: staticProductPredicate);        */

        /* Reference method com método não estático
        list.removeIf (Product :: nonStaticProductPredicate);       */

        /*  Expressão lambda declarada
       Predicate<Product> pred = p -> p.getPrice() >= 100.0;
       list.removeIf(pred);                    */


        /*  Expressão lambda inline
        double min = 100.0;
        list.removeIf(p -> p.getPrice() >= min);             */

        for (Product p: list) {
            System.out.println(p);

    }

    }
}

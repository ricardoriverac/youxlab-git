package curso_completo_java.sessao_18.pratica.exemplo_pratica03.util;

import curso_completo_java.sessao_18.pratica.exemplo_pratica03.entities.Product;

import java.util.function.Predicate;

public class ProductPredicate implements Predicate<Product> {


    @Override
    public boolean test(Product p) {
        return p.getPrice() >= 100.0;
    }
}

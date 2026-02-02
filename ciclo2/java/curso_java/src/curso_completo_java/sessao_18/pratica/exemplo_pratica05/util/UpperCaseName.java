package curso_completo_java.sessao_18.pratica.exemplo_pratica05.util;

import curso_completo_java.sessao_18.pratica.exemplo_pratica05.entities.Product;

import java.util.function.Function;

public class UpperCaseName implements Function<Product, String> {

    @Override
    public String apply(Product p) {
        return p.getName().toUpperCase();
    }
}

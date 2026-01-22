package curso_completo_java.sessao_18.pratica.exemplo_pratica04.util;


import curso_completo_java.sessao_18.pratica.exemplo_pratica04.entities.Product;

import java.util.function.Consumer;

public class PriceUpdate implements Consumer<Product> {

        @Override
        public void accept (Product p) {
            p.setPrice(p.getPrice() * 1.1);
        }
}

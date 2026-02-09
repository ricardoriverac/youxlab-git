package secao18_ProgramacaoFuncional.testes.function;

import java.util.function.Function;

public class UpperCaseName implements Function<Product, String> {
    @Override
    public String apply(Product p) {
        return p.getNome().toUpperCase();
    }
}

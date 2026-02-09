package secao18_ProgramacaoFuncional.testes.predicate;

public class ProductPredicate implements Predicate<Produto>{

    @Override
    public boolean test(Produto produto) {
        return produto.getPreco() >= 100;
    }
}

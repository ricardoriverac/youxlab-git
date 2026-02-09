package secao18_ProgramacaoFuncional.testes.comparator;

import java.util.Comparator;

public class Comparato implements Comparator<Produto> {

    @Override
    public int compare(Produto p1, Produto p2) {
        return p1.getPreco().compareTo(p2.getPreco());
    }
}

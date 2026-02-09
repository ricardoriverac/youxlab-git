package secao18_ProgramacaoFuncional.testes.predicate;

import secao18_ProgramacaoFuncional.testes.comparator.Comparato;
import secao18_ProgramacaoFuncional.testes.comparator.Produto;

import java.util.ArrayList;
import java.util.List;

public class program {
    public static void main(String[] args) {
        List<Produto> list = new ArrayList<>();

        list.add(new Produto<>("TV", 2000.00));
        list.add(new Produto<>("Gengibre", 1.50));
        //sei o que deu errado nn
        for (Produto p : list){
            System.out.println(p);
        }
    }
}

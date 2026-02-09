package secao18_ProgramacaoFuncional.testes.comparator;

import java.util.ArrayList;
import java.util.List;

public class program {
    public static void main(String[] args) {
        List<Produto> list = new ArrayList<>();

        list.add(new Produto<>("TV", 900.00));
        list.add(new Produto<>("Notebook", 1200.00));
        list.add(new Produto<>("Tablet", 450.00));

        list.sort(new Comparato());

        for (Produto p : list){
            System.out.println(p);
        }
    }
}

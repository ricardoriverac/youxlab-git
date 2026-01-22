package ProgramacaoFuncionalExpressaoLambda.application;

import ProgramacaoFuncionalExpressaoLambda.entities.Product;

import java.util.ArrayList;
import java.util.List;

public class Program {

    static void main() {

        List<Product> produtos = new ArrayList<>();

        produtos.add(new Product("TV", 900.00));
        produtos.add(new Product("Notebook", 1200.00));
        produtos.add(new Product("Tablet", 450.00));

        produtos.sort((p1, p2) -> p1.getName().toUpperCase().compareTo(p2.getName().toUpperCase()));

        for (Product p : produtos) {
            System.out.println(p);
        }

    }
}

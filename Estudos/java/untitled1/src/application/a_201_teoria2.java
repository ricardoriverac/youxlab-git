package application;

import application.entities.Produto;

import java.util.ArrayList;
import java.util.List;

public class a_201_teoria2 {
    public static int compareProducts(Produto p1, Produto p2){
        return p1.getPreco().compareTo(p2.getPreco());
    }
    public static void main(String[] args) {
            List<Produto> produtos = new ArrayList<>();

            produtos.add(new Produto("TV", 900.00));
            produtos.add(new Produto("Notebook", 1200.00));
            produtos.add(new Produto("Tablet", 450.00));

            produtos.sort(a_201_teoria2::compareProducts);

            produtos.forEach(System.out::println);
    }
}

package application;

import application.entities.Produto;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class a_205 {
    public static void main(String[] args) {

        List<Produto> produtos = new ArrayList<>();

        produtos.add(new Produto("Tv", 900.0));
        produtos.add(new Produto("Mouse", 50.00));
        produtos.add(new Produto("Tablet", 350.50));
        produtos.add(new Produto("HD case", 80.90));

        List<String> nomes = produtos.stream().map(p -> p.getNome().toUpperCase()).toList();
        nomes.forEach(System.out::println);
    }
}

package application;

import application.entities.Produto;
import application.entities.ServicoProduto;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

public class a_206 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        List<Produto> produtos = new ArrayList<>();

        produtos.add(new Produto("TV", 900.00));
        produtos.add(new Produto("Mouse", 50.00));
        produtos.add(new Produto("Tablet", 350.50));
        produtos.add(new Produto("HD Case", 80.90));

        ServicoProduto sp = new ServicoProduto();
        double soma = sp.filteredSum(produtos, p -> p.getNome().charAt(0) == 'T');
        System.out.println("Soma: " + String.format("%.2f", soma));

    }
}

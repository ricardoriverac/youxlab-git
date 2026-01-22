package curso_completo_java.sessao_17.pratica.exemplo_pratica07.application;

// AULA 192 - Como Set testa igualdade

import curso_completo_java.sessao_17.pratica.exemplo_pratica07.entities.Product;

import java.util.HashSet;
import java.util.Set;

public class program {

    public static void main(String[] args) {

        Set<Product> set = new HashSet<>();

        set.add(new Product("TV", 900.0));
        set.add(new Product("Notebook", 1200.0));
        set.add(new Product("Tablet", 400.0));

        Product prod = new Product("Notebook", 1200.0);
        System.out.println(set.contains(prod));
    }
}

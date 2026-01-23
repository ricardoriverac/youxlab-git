package curso_completo_java.sessao_18.pratica.exemplo_pratica06.application;

// AULA 206 - 206. Criando funções que recebem funções como parâmetro

import curso_completo_java.sessao_18.pratica.exemplo_pratica06.entities.Product;
import curso_completo_java.sessao_18.pratica.exemplo_pratica06.model.service.ProductService;

import java.util.ArrayList;
import java.util.List;

public class program {

    public static void main(String[] args) {

        List<Product> list = new ArrayList<>();
        list.add(new Product("Tv", 900.00));
        list.add(new Product("Mouse", 50.00));
        list.add(new Product("Tablet", 350.50));
        list.add(new Product("HD Case", 80.90));

      /*  ProductService ps = new ProductService();
        double sum = ps.filteredSum(list);
        System.out.println("Sum =" + String.format("%.2f", sum));*/

        ProductService ps = new ProductService();
        double sum = ps.filteredSum(list, p -> p.getPrice() < 100.0);
        System.out.println("Sum =" + String.format("%.2f", sum));
    }
    }





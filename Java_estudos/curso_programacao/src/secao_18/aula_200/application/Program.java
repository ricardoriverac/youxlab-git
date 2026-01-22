package secao_18.aula_200.application;

import secao_17.aula_187.entities.Product;

import java.util.*;

public class Program {
    public static void main(String[] args) {
        List<Product> list = new ArrayList<>();

        list.add(new Product("TV", 900.00));
        list.add(new Product("Notebook", 1200.00));
        list.add(new Product("Tablet", 450.00));

        Comparator<Product> comp = (p1,p2) ->{
            return p1.getName().toUpperCase().compareTo(p2.getName().toUpperCase());
        };
        list.sort(comp);

        for (Product p : list){
            System.out.println(p);
        }



    }
}

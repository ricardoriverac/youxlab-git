package application;

import application.entities.Produto;

import java.util.ArrayList;
import java.util.List;

public class a_203 {
    public static void main(String[] args) {

        List<Produto> list = new ArrayList<>();

        list.add(new Produto("TV", 900.00));
        list.add(new Produto("Mouse", 50.00));
        list.add(new Produto("Tablet", 350.50));
        list.add(new Produto("HD case", 80.90));

        double min = 100.00;

        list.removeIf(p -> p.getPreco() >= min);
        for(Produto p : list){
            System.out.println(p);
        }
    }
}

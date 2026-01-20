package application;

import application.entities.Produto;

import java.util.HashSet;
import java.util.Set;

public class a_192 {
    public static void main(String[] args) {
        Set<Produto> set = new HashSet<>();

        set.add(new Produto("TV", 900.0));
        set.add(new Produto("Notebook", 1200.0));
        set.add(new Produto("Tablet", 400.0));
        set.add(new Produto("Tablet", 400.0));

        Produto produto = new Produto("Notebook", 1200.0);

        System.out.println(set.contains(produto));
    }
}
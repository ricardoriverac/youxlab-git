package application;

import application.entities.Produto;

import java.util.Map;
import java.util.TreeMap;

public class a_196_pt2 {
    public static void main(String[] args) {
        Map<Produto, Double> map = new TreeMap<>();
        Produto p1 = new Produto("Tv", 900.0);
        Produto p2 = new Produto("Notebook", 1200.0);
        Produto p3 = new Produto("Tablet", 400.0);

        map.put(p1, 10000.0);
        map.put(p2, 20000.0);
        map.put(p3, 15000.0);

        Produto ps = new Produto("Tv", 900.0);

        System.out.println("Existe a chave 'ps': " + map.containsKey(ps));
    }
}

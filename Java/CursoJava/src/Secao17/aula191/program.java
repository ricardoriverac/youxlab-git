package Secao17.aula191;

import java.util.Arrays;
import java.util.Set;
import java.util.TreeSet;

public class program {
    public static void main(String[] args) {
            Set<Integer> a = new TreeSet<>(Arrays.asList(0,2,4,5,6,8,10));
            Set<Integer> b = new TreeSet<>(Arrays.asList(5,6,7,8,9,10));
            Set<Integer> c = new TreeSet<>(a);
            c.addAll(b);
            System.out.println(c);
            Set<Integer> d = new TreeSet<>(a);
            d.retainAll(b);
            System.out.println(d);
            Set<Integer> e = new TreeSet<>(a);
            e.removeAll(b);
            System.out.println(e);
        }

    public static class Product {
        private String name;
        private Double price;

        public Product(String name, Double price) {
            this.name = name;
            this.price = price;
        }
        public String getName() {
            return name;
        }
        public void setName(String name) {
            this.name = name;
        }
        public Double getPrice() {
            return price;
        }
        public void setPrice(Double price) {
            this.price = price;
        }
    }
}


package application;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;
import java.util.stream.Collectors;

public class a_105 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<String> list = new ArrayList<>();

        list.add("Maria");
        list.add("Alex");
        list.add("Bob");
        list.add("Anna");

        for(String x : list){
            System.out.println(x);
        }
        list.add(2, "Joao");
        System.out.println(list.size());
        list.removeIf(x -> x.charAt(0) == 'M');
        for(String x : list){
            System.out.println(x);
        }
        System.out.println("-------------------");
        System.out.println(list.indexOf("Bob"));
        System.out.println(list.indexOf("Maria"));
        List<String> result = list.stream().filter(x -> x.charAt(0) == 'A').collect(Collectors.toList());
        for (String x : result){
            System.out.println(x);
        }
        System.out.println("--------------------");
        String nome = list.stream().filter(x -> x.charAt(0) == 'A').findFirst().orElse(null);
        System.out.println(nome);
    }
}

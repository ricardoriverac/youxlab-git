package Aula_105.Listas.Lista_parte2;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<String> list = new ArrayList<>();

        list.add("Elisa");
        list.add("Pedro");
        list.add("Otto");
        list.add("Raicony");

        list.add(2, "Juan");

        for (String p : list) {
            System.out.println(p);
        }

        System.out.print(list.size());



    }
}

package Secao_17.Aula_192.Set.LinKedHashSet;

import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {

        //LinKedHashSet - velocidade intermediária e elementos na ordem em que são adicionadas

        // Ele mantem a ordem

        Set<String> set = new LinkedHashSet<>();

        set.add("TV");
        set.add("Tablet");
        set.add("Notebook");

        System.out.println(set.contains("Notebook"));

        for (String p : set) {
            System.out.println(p);
        }
    }
}

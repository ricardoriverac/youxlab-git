package Secao_17.Aula_192.Set.TreeSet;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {

        //TreeSet - mais lento e ordenado pelo compareTo do objeto
        //Ordena em ondem alfabetica - obs: as letras maiuscula vem 1° que as minusculas

        Set<String> set = new TreeSet<>();

        set.add("TV");
        set.add("Tablet");
        set.add("Notebook");

        System.out.println(set.contains("Notebook"));

        for (String p : set) {
            System.out.println(p);
        }
    }
}

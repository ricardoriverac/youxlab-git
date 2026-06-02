package Secao_17.Aula_192.Set.HashSet;

import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        // Set<T> Representa um conjunto de elementos (Similar a uma lista)
            // Não permite repetições
            // elementos não possuem posição
            // Acesso, inserção e remoção de elementos são rápidos
            // Oferece operações eficientes de conjunto: interseção, união, diferença


        // Principais implementações:

        //HashSet - Mais rápido e não ordenada

        Set<String> set = new HashSet<>();

        set.add("TV");
        set.add("Tablet");
        set.add("Notebook");

        set.removeIf(x -> x.length() >= 3);

        for (String p : set) {
            System.out.println(p);
        }
    }
}

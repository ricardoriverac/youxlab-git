package Secao_17.Aula_189.Tipos_Curinga.applications;

import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> myInts = Arrays.asList(5, 2, 10);
        printList(myInts);

        List<String> myStrings = Arrays.asList("Elisa", "Pedro", "Juan");
        printList(myStrings);
    }
    public static void printList(List<?> list) {
        for (Object obj : list) {
            System.out.println(obj);
        }
    }
}

package Secao17.aula188;

import java.util.Arrays;
import java.util.List;

public class Program1 {
    public static void main(String[] args) {
        // um genérico de "qualquer tipo"
        List<Integer> myInts = Arrays.asList(5, 2, 10);
        printList(myInts);
    }
    public static void printList(List<?> list) {
        for (Object obj : list) {
            System.out.println(obj);
        }
    }
}

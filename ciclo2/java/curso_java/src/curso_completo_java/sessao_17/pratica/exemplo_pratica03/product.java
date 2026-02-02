package curso_completo_java.sessao_17.pratica.exemplo_pratica03;

import java.util.Arrays;
import java.util.List;

public class product {

        public static void main(String[] args) {
            List<Integer> myInts = Arrays.asList(5, 2, 10);
            printList(myInts);

            List<String> myStrs = Arrays.asList("Maria, Alex, Bob");
            printList(myStrs);
        }
    public static void printList(List<?> list) {
        for (Object obj : list) {
            System.out.println(obj);
        }
    }

    }

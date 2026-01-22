package curso_completo_java.sessao_17.pratica.exemplo_pratica06.exemplo1;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class program {

    public static void main(String[] args) {

        Set<String> set = new LinkedHashSet<>();

        // HashSet → não garante a ordem
        // TreeSet → ele ordena
        // LinkedHashSet → mantem a ordem

        set.add("TV");
        set.add("Notebook");
        set.add("Tablet");

        //set.removeIf(x -> x.length() >= 3);
        //set.removeIf(x -> x.charAt(0) == 'T');

        for (String p : set) {
            System.out.println(p);
        }
    }
}

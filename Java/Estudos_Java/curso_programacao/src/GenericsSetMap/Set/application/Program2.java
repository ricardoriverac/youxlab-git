package GenericsSetMap.Set.application;

import java.util.Arrays;
import java.util.Set;
import java.util.TreeSet;

public class Program2 {

    static void main() {

        Set<Integer> a = new TreeSet<>(Arrays.asList(0,2,4,5,6,8,10));
        Set<Integer> b = new TreeSet<>(Arrays.asList(5,6,7,8,9,10));

        //união
        Set<Integer> c = new TreeSet<>(a);
        c.addAll(b);
        System.out.println("União -> " + c);

        //interseção
        Set<Integer> d = new TreeSet<>(a);
        d.retainAll(b);
        System.out.println("Interseção -> " + d);

        //diferença
        Set<Integer> e = new TreeSet<>(a);
        e.removeAll(b);
        System.out.println("Diferença -> " + e);
    }
}

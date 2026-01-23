package secao10_Java.listas;

import java.util.ArrayList;
import java.util.List;

public class listas1 {
    public static void main(String[] args){
        List<String> list = new ArrayList<>();

        list.add("Maria");
        list.add("ALex");
        list.add("Bob");
        list.add("Anna");
        list.add(2, "Marco");
        list.remove("Anna");
        //função Lambda
        list.removeIf(x -> x.charAt(0) == 'M');
        System.out.println(list.size());
        for(String x : list) {
            System.out.print(x);
        }
    }

}

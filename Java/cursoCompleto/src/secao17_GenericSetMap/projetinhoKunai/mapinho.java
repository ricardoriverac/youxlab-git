package secao17_GenericSetMap.projetinhoKunai;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class mapinho {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Map<String, String> map = new HashMap<>();

        System.out.println("Enter KEY: ");
        String key = sc.next();
        System.out.println("Enter VALUE: ");
        String value = sc.next();
        map.put(key, value);
        for (String kei: map.keySet()){
            System.out.println(kei + " "+ map.get(kei));
        }

    }
}

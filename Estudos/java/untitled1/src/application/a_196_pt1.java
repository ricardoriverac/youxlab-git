package application;

import java.util.Map;
import java.util.TreeMap;

public class a_196_pt1 {
    public static void main(String[] args) {

        Map<String, String> map = new TreeMap<>();

        map.put("username", "maria");
        map.put("email", "maria@gmail.com");
        map.put("phone", "99771122");

        map.remove("email");
        map.put("phone", "99771133");

        System.out.println("Existe a chave key" + map.containsKey("phone"));
        System.out.println("Número de celular" + map.get("phone"));
        System.out.println("Email: " + map.get("email"));
        System.out.println("Tamnho: " + map.size());

        System.out.println("Todos os cookies: ");
        for(String key : map.keySet()){
            System.out.println("key: " + map.get(key));
        }
    }
}

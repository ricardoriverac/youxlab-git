package Secao_17.Aula_197.Map.applications;

import java.util.Map;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) {

        Map<String, String> cookies = new TreeMap<>();

        cookies.put("username", "Maria");
        cookies.put("email", "maria@gmail.com");
        cookies.put("phone","99711122");

        cookies.remove("email");
        cookies.put("phone", "99771133");

        System.out.println("Contém a tecla 'phone': " + cookies.containsKey("phone"));
        System.out.println("Numero do 'phone': " + cookies.get("phone"));
        System.out.println("Email: " + cookies.get("email"));
        System.out.println("Size: " + cookies.size());

        System.out.println("\nTODOS COOKIES: ");
        for (String key : cookies.keySet()) {
            System.out.println(key + ": " + cookies.get(key));
        }
    }
}

package GenericsSetMap.hashCode_Equals.Personalizados.application;

import GenericsSetMap.hashCode_Equals.Personalizados.entities.Client;

import java.util.concurrent.Callable;

public class Program {

    static void main() {

        Client c1 = new Client("Maria", "maria@gmail.com");
        Client c2 = new Client("Maria", "maria@gmail.com");

        String s1 = new String("Text");
        String s2 = new String("Text");

        System.out.println(c1.hashCode());
        System.out.println(c2.hashCode());
        System.out.println(c1.equals(c2));
        System.out.println(c1 == c2);
        System.out.println(s1 == s2);
    }
}

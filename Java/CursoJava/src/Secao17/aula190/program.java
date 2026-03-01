package Secao17.aula190;

public class program {
    public static void main(String[] args) {
            Client c1 = new Client("Maria", "maria@gmail.com");
            Client c2 = new Client("Maria", "maria@hotmail.com");
            String s1 = "Test 1" ;
            String s2 = "Test 2";

            System.out.println("c1.hashCode() = " + c1.hashCode());
            System.out.println("c2.hashCode() = " + c2.hashCode());
            System.out.println("c1.equals(c2) = " + c1.equals(c2));
            System.out.println(c1 == c2);
            System.out.println(s1 == s2);

    }
    }


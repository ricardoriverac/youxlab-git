package Topios_basios_java.Funcoes_String._split;

public class codigo_split {
    static void main() {
        String s = "potato apple lemon orange";
        String[] vect = s.split(" ");
        System.out.println(vect[0]);
        System.out.println(vect[1]);
        System.out.println(vect[2]);
        System.out.println(vect[3]);
    }
}

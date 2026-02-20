package Aula_66.Funcoes_interessantes_para_String;

public class Aula_05_split {
    public static void main(String[] args) {
        // split

        /*Serve para separar as palavras dentro da string*/

        String palavra = "Limão Abobora Abacaxi Amora";

        String[] vect = palavra.split(" ");

        String p1 = vect[0];
        String p2 = vect[1];
        String p3 = vect[2];
        String p4 = vect[3];

        System.out.println(p3);
    }
}
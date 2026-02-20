package Aula_66.Funcoes_interessantes_para_String;

public class Aula_04_Buscar {
    public static void main(String[] args) {
        // Buscar

        String palavra = "Java HTML CSS Python php";

        /*indexof("ab"): Mostra qual foi a 1º vez que
          a determinada string aparece na frase
          Exemplo:   */

        System.out.println(palavra.indexOf('a'));


        /*lastIndexOf("ab"): mostra a ultima ves que apareceu
        a palavra na string
        Exemplo:         */

        System.out.println(palavra.lastIndexOf("a"));


    }
}
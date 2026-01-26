package Aula_66.Funcoes_interessantes_para_String;

public class Aula_03_Recortar {
    public static void main(String[] args) {

        String palavra = "Substituir palavras ou letras";
        //Substituir

        /*replace('a', 'x'): Serve para substituir uma
          letra/palavra ('a') opor outra ('x'), também pode
          Exemplo:    */

        System.out.println(palavra.replace('a', 'x'));

        System.out.println(palavra.replace("palavras", "mecanicas"));
    }
}
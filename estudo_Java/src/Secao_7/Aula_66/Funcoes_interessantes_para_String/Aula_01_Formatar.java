package Aula_66.Funcoes_interessantes_para_String;

public class Aula_01_Formatar {
    public static void main(String[] args) {

        // Formata uma String

        /*toLowerCase(): Transforma a String em minusculo

          toUpperCase(): Deixa a String em maiusculo

           trim: Remove os espaços  que vem antes e depois

           Exemplo: */

        String p = "     abcde FGHIJ abc DEFG   ";

        System.out.println("-" + p.toLowerCase() + "-");
        System.out.println("-" + p.toUpperCase() + "-");
        System.out.println("-" + p.trim() + "-");

    }
}

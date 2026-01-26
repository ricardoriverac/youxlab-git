package Aula_66.Funcoes_interessantes_para_String;

public class Aula_02_Recortar {
    public static void main(String[] args) {

        //Recortar

        String palavra = "ABCD efgh IJKL mnop";

        /* substring(inicio): Serve para pegar uma parte de
        uma string, ele pega uma determinada letra da string
        e mostra adiante

        Exemplo:*/

        System.out.println(palavra.substring(5));

        /* substring(inicio, fim): ele pega uma determinada
        letra da string e vai ate a ultima, sem mostrar ela

        Exemplo:*/

        System.out.println(palavra.substring(3, 10));
    }
}
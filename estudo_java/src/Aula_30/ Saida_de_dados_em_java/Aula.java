package Aula_30_Saida_de_dados_em_java;

import java.util.Locale;

public class Aula {
    public static void main(String[] args) {

        //Aparição no terminal

        // Println:

        System.out.println("Olá, Mundo");

        /*O comando "println" acima, serve
          para fazer valores no terminal,
          independente do valor*/

        // Print:

        System.out.print("Bom dia!!");

        /* O comando "print" a cima, serve
        para quebrar linha, inves de
        aparecer um em baixo do outro,
        aparece um do lado do outro
         */
        System.out.print(" Ola!!");

        // Variavel
        double y = 8.3472;
        System.out.println(y);

        // Printf:

        System.out.printf("%.2f%n", y);

        /*O printf serve para só que formatado*/
        /*Obs: O "%.2f" serve para mostrar quatos
          numero depois da virgula deseja que apareça*/

        // Locale:
        /*Locale serve para mudar a localização
          do computador */

        Locale.setDefault(Locale.US);
        System.out.printf("%.4f%n", y);

        /* O locale necessita de uma importação
        para funcionar */

        // Concatenação
        /* Para concatenar variaveis em
          uma frase só, vocẽ deve utilizar
          p "printf" */

        String nome = "Ercules";
        int idade = 103;
        System.out.printf("A %s tem %d", nome, idade);

        /*Para isso o usuário deve utilizar
          %f, %d, %s e o  %n, e deve também
          colocar em ordem que estiver após
          a virgula, tem que colocar dentro
          dos parenteses
        */

        /*Tabela:
        %f -> ponto flutuante
        %d -> inteiro
        %s -> texto
        %n -> quebra linha
         */


    }
}
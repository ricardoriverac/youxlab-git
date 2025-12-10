package Estrutura_condicional05.pratica;

/* AULA 44 - Sintaxe opcional - swich-case */


/* Fazer um programa para ler um valor inteiro de 1 a 7 representando um dia da semana (sendo 1=domingo, 2=segunda, e assim por diante).
Escrever na tela o dia da semana correspondente, conforme exemplos.*/

import java.util.Scanner;

public class pratica_exemplo04 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


        int x = sc.nextInt();
        String dia;

        if (x == 1) {
            dia = "domingo";
        }
        else if (x == 2) {
            dia = "segunda";
        } else if (x == 3) {
            dia = "terça";
        } else if (x== 4) {
            dia = "quarta";
        } else if (x == 5) {
            dia = "quinta";
        } else if (x == 6) {
            dia = "sexta";
        } else if (x == 7) {
            dia = "sabádo";
        }
        else {
            dia = "valor inválido";
        }

        System.out.println("Dia da semana: "+dia);

    }

}

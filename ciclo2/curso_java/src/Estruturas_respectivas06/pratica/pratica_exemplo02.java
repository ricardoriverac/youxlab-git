package Estruturas_respectivas06.pratica;

/*Fazer um programa que lê números inteiros até que um zero seja lido. Ao
final mostra a soma dos números lidos.*/

import java.util.Scanner;

public class pratica_exemplo02 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();

        while (x != 0) {
            x = sc.nextInt();
        }

        sc.close();
    }
}

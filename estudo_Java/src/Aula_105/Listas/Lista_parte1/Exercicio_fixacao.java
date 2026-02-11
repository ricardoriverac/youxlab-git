package Aula_105.Listas.Lista_parte1;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercicio_fixacao {
    public static void main(String[] args) {

        List<Integer> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        int maiorNumero = 0;

        System.out.println("Digite 5 números");

        for (int i=0; i<5; i++) {
            list.add(sc.nextInt());
        }

        for (int n : list) {
            if (n>0) {
                maiorNumero = n;
            }
        }

        System.out.println("Maior número = " + maiorNumero);
    }
}

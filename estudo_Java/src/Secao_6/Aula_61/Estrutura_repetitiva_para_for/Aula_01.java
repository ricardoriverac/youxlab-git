package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Scanner;

public class Aula_01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int x = 0;
        int y = 10;

        System.out.print("Digite um valor: ");
        x = sc.nextInt();

        for (int z=1; x < y; x ++){
            z = (z + x);
            System.out.print(z + " " );
            System.out.print(y + " ");
            System.out.println(x);
        }
    }
}
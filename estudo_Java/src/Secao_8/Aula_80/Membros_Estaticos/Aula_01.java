package Aula_80.Membros_Estaticos;

import java.util.Scanner;

public class Aula_01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int valor = sc.nextInt();
        System.out.println( par_impar(valor));
    }

    public static int par_impar(int x) {

        if (x % 2 == 0) {
            System.out.print("Par - ");
        }
        else {
            System.out.print("Impar - ");
        }
        return x;
    }
}

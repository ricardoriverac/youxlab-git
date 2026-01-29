package Secao6.Aula55;

import java.util.Scanner;

public class Aula55_exercicio1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a senha de acesso: ");
        int x = sc.nextInt();
        if (x != 2002) {
            System.out.print("Senha Invalida");
        }
        else{
            System.out.print("Acesso Permitido");

        }


        sc.close();
    }
}

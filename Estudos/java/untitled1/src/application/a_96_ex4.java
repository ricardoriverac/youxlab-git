package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex4 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Caro usuário, por favor insira quantos números você deseja verificar: ");
        int quantidadeNumeros = sc.nextInt();

        int[] numero = new int[quantidadeNumeros];
        for (int i = 0; i < numero.length; i++) {
            System.out.printf("Caro usuário, por favor insira o %d número que você deseja verificar: ", i+1);
            numero[i] = sc.nextInt();
        }
        int countPares = 0;
        System.out.print("Números pares: ");
        for (int i = 0; i < numero.length; i++) {
            if(numero[i] % 2 == 0){
                 countPares+=1;
                System.out.printf("%d, ", numero[i]);
            }
        }
        System.out.printf("Quantidade de números pares: %d", countPares);
    }
}

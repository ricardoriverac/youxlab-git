package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Scanner;

public class Exercicio_02 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int in = 0, out = 0, n, c = 1;

        System.out.printf("Digite o %dº valor: ",c);
         n = sc.nextInt();

        for (int i = 0; i < 5; i++ ) {
            c++;
            if (n >= 10 && n <= 20) {
                in++;
            }
            else{
                out++;
            }

            System.out.printf("Digite o %dº valor: ", c);
            n = sc.nextInt();
        }

        System.out.printf("%d in %n",in);
        System.out.printf("%d out",out);
    }
}
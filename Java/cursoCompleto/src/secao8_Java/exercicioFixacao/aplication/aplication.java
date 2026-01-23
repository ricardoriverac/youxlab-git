package secao8_Java.exercicioFixacao.aplication;

import secao8_Java.exercicioFixacao.mets.met1;

import java.util.Locale;
import java.util.Scanner;

public class aplication {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        met1 met1;

        System.out.print("COLOQUE O NÚMERO DA CONTA: ");
        int numero = sc.nextInt();
        System.out.print("COLOQUE O NOME DA CONTA: ");
        String nome = sc.next();
        System.out.print("Deseja executar algum depósito inicial na conta? [S/N]");
        char resp = sc.next().charAt(0);
        if (resp != 'S') {
            met1 = new met1(nome, numero);
        }
        else {
            System.out.print("Defina o valor do depósito inicial: ");
            double quantidade = sc.nextDouble();
            met1 = new met1(nome, numero, quantidade);
        }
        System.out.print(met1);

        sc.close();
    }
}

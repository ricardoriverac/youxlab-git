package application;

import application.entities.ServicoImpressora;

import java.util.Locale;
import java.util.Scanner;

public class a_186 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ServicoImpressora<Integer> si = new ServicoImpressora<>();

        System.out.println("Caro usuário, quantos valores serão digitados: ");
        Integer quantidadeNumeros = sc.nextInt();

        for (int i = 0; i < quantidadeNumeros; i++) {
            Integer valor = sc.nextInt();
            si.addValor(valor);
        }
        si.imprimir();
        Integer x = si.primeiro();
        System.out.println("Primeiro: " + x);

        sc.close();
    }
}

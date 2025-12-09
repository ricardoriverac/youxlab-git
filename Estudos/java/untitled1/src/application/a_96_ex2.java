package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, por favor insira quantos números você deseja inserir: ");
        int limite = sc.nextInt();

        double[] vect = new double[limite];
        for (int i = 0; i < vect.length; i++) {
            System.out.printf("Caro usuário, por favor digite um dos %d números", vect.length);
            vect[i] = sc.nextDouble();
        }

        double soma = 0.0;
        for (int i = 0; i < vect.length; i++) {
            soma+=vect[i];
        }
        double avg = soma / vect.length;

        System.out.print("Valores: ");
        for (int i = 0; i < vect.length; i++) {
            System.out.printf("%.2f, ", vect[i]);
        }
        System.out.println("Soma: " + soma);
        System.out.println("Média: " + avg);
    }
}

package Aula_97.Vetores.Exercicio_pensionato;

import java.lang.Class;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a quantidade de cadastros: ");
        int n = sc.nextInt();

        Classe[] vect = new Classe[10];

        int numeroQuarto;
        String nome;
        String Gmail;
        int c = 0;

        for (int i=0; i<n; i++) {
            c++;

            System.out.printf("%nDigite o %d° cadastro: %n", c);
            System.out.print("Nome: ");
            sc.nextLine();
            nome = sc.nextLine();

            System.out.print("Email: ");
            Gmail = sc.nextLine();

            System.out.print("Numero do quarto: ");
            numeroQuarto = sc.nextInt();

            vect[numeroQuarto] = new Classe(numeroQuarto, nome, Gmail);
        }

        System.out.printf("%n Quartos ocupados: %n");
        for (int i = 0; i < vect.length; i++) {
            if (vect[i] != null){
                System.out.println(i + ": " + vect[i].getNome() + ", " + vect[i].getGmail());
            }
        }


    }
}

package application;

import application.entities.Quarto;

import java.util.Locale;
import java.util.Scanner;

public class a_99_desafioPensionato {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Quarto[] vect = new Quarto[10];

        System.out.print("Caro usuário, por favor insira quantos estudantes vão alugar um dos 10 quartos: ");
        int quantidadeEstudantes = sc.nextInt();


        Integer numQuarto = 0;
        for (int i = 0; i < quantidadeEstudantes; i++) {
            System.out.printf("\n Caro usuário, por favor informe qual dos 10 quartos diponíveis o %do estudante deseja alugar: ", i+1);
            numQuarto = sc.nextInt();
            sc.nextLine();
            System.out.printf("Caro usuário, por favor informe o nome do %do estudante ", i+1);
            String nome = sc.nextLine();
            System.out.printf("\nCaro usuário, por favor informe também o email do %do estudante ", i+1);
            String email = sc.nextLine();
            vect[numQuarto] = new Quarto(nome, email);
        }
        System.out.println("Quartos alugados: ");
        for (int i = 0; i < vect.length; i++) {
            if(vect[i] != null){
                System.out.println(i + ": " + vect[i]);
            }
        }
    }
        
}

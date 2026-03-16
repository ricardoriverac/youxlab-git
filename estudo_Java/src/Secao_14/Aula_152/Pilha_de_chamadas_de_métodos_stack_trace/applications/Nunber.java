package Secao_14.Aula_152.Pilha_de_chamadas_de_métodos_stack_trace.applications;

import java.util.Scanner;

public class Nunber {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


        try {
            System.out.print("Digite um número inteiro: ");
            int numeroInteiro = sc.nextInt();
        }
        catch (Exception e) {
            System.out.println("ERRO!!");
            e.printStackTrace();
        }
    }
}

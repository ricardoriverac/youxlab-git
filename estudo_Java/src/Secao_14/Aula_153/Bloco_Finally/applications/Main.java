package Secao_14.Aula_153.Bloco_Finally.applications;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try{
            System.out.printf("Digite o 1° número: ");
            int numero1 = sc.nextInt();

            System.out.print("Digite o 2° número: ");
            int numero2 = sc.nextInt();

            int divisao = numero1 / numero2;
        }
        catch (Exception e) {
            System.out.println("ERRO!!");
            e.printStackTrace();
        }
        finally{
            System.out.println("Programa finalizado !!");
        }
    }
}

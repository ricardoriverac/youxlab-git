package Aula_46.Sintaxe_opcional;

import java.util.Scanner;

public class Aula_01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int dia = sc.nextInt();

        switch (dia) {
            case 1:
                System.out.println("Domingo");
                break;
            case 2:
                System.out.println("Segunda-feira");
                break;
            case 3:
                System.out.println("Terça-feira");
                break;
            case 4:
                System.out.println("Quarta-feira");
                break;
            default:
                System.out.println("Dia inválido");
        }
    }
}


package Secao5.Aula42;

import java.util.Scanner;

public class aula42 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hora;
        System.out.println("Quantas horas?");
        hora = sc.nextInt();
        if (hora < 12) {
            System.out.print("Bom dia");
        }
        else {
            System.out.print("Boa tarde");
        }
            sc.close();
        }

    }

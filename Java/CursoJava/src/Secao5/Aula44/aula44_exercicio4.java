package Secao5.Aula44;

import java.util.Scanner;

public class aula44_exercicio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hora_inicial, hora_final;
        System.out.print("Informe a horas que iniciou: ");
        hora_inicial = sc.nextInt();
        System.out.print("Informe a horas que encerrou: ");
        hora_final = sc.nextInt();
        int duracao;
        if (hora_inicial < hora_final) {
            duracao = hora_final - hora_inicial;
        }
        else {
                duracao = (24 - hora_inicial) + hora_final;
            }
        System.out.println("O jogo durou " + duracao);

        }
    }


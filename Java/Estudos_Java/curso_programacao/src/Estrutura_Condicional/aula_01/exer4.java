package Estrutura_Condicional.aula_01;

import java.util.Scanner;

public class exer4 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int horaI, horaF, tempo;
        System.out.println("Hora de inicio:");
        horaI = sc.nextInt();
        System.out.println("Hora final:");
        horaF = sc.nextInt();
        if (horaI > horaF) {
            tempo = horaI - horaF;
        }
        else {
            tempo = 24 - horaF + horaI;
        }
        System.out.println("O jogo durou " + tempo + " hora(s)");
    }
}

package secao5_estrutura_condicional.exercicios_elif;

import java.util.Scanner;

public class exercicio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite a hora que o jogo começou:");
        int hi = sc.nextInt();
        System.out.println("Digite a hora que o jogo terminou:");
        int hf = sc.nextInt();

        int duracao;
        if (hf > hi) {
            duracao = hf - hi;
        }
        else {
            duracao = 24 - hf + hi;
        }
        System.out.println("A duração do jogo foi de " + duracao + " horas");
    }
}

package secao_05;

import java.util.Scanner;

public class exercicio_04 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int inicio = sc.nextInt();
        int hrfinal = sc.nextInt();
        int duracao;
        if (inicio < hrfinal) {
            duracao = hrfinal - inicio;
        }
        else {
            duracao = 24 - inicio + hrfinal;
        }

        System.out.println("O jogo durou " + duracao + " hora(s)");

        sc.close();


    }
}

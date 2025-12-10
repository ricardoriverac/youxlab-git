package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex5 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Caro usuário, por favor insira quantas posições você deseja verificar: ");
        int quantidadeṔosicoes = sc.nextInt();;
        double[] posicao = new double[quantidadeṔosicoes];
        for (int i = 0; i < quantidadeṔosicoes; i++) {
            System.out.printf("Caro usuário, por favor digite sua %da posição", i+1);
            posicao[i] = sc.nextInt();
        }
        double maior = 0;
        int maiorIndice = 0;
        System.out.print("Maior valor: ");
        for (int i = 0; i < quantidadeṔosicoes; i++) {
            if (posicao[i] > maior){
                maior = posicao[i];
                maiorIndice = i;
            }
        }
        System.out.printf("%.2f\n", maior);
        System.out.printf("Posição do maior valor: %d", maiorIndice);



    }
}

package secao7_introOrientacaoaObjetos.exercicios.exercicio1;

import java.util.Scanner;

public class exercicio1 {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        metodos1 met = new metodos1();

        System.out.println("COLOQUE A LARGURA E A ALTURA: ");
        met.Width = sc.nextDouble();
        met.height = sc.nextDouble();
        System.out.println(met);
    }
}

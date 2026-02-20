package Aula_109.Matrizes;

public class Exercicio_01 {
    public static void main(String[] args) {

        int[][] matriz = new int[2][2];

        matriz[0][0] = 10;
        matriz[0][1] = 20;
        matriz[1][0] = 30;
        matriz[1][1] = 40;

        System.out.println("Valor matriz[0][0]: " + matriz[0][0]);
        System.out.println("Valor matriz[1][1]: " + matriz[1][1]);

        int soma = matriz[0][0] + matriz[0][1] + matriz[1][0] + matriz[1][1];
        System.out.println("Valor  total " +  soma);

        matriz[0][1] = 100;

        System.out.println("Valor matriz[0][1]: "  + matriz[0][1]);


    }
}

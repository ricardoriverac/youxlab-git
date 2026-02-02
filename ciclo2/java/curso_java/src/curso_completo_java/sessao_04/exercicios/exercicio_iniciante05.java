package curso_completo_java.sessao_04.exercicios;

/* Fazer um programa para ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o
código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Calcule e mostre o valor a ser pago.
*/

import java.util.Scanner;

public class exercicio_iniciante05 {

    public static void main(String[] ags){

        Scanner sc = new Scanner(System.in);

        int codigo_peca1, numero_peca1, codigo_peca2, numero_peca2;
        double preco_peca1, preco_peca2;
        double valor_pagar;

        System.out.println("Digite o código da peça 1:");
        codigo_peca1 = sc.nextInt();
        System.out.println("Digite a quantidade de peças da peça 1:");
        numero_peca1 = sc.nextInt();
        System.out.println("Digite o valor da peça 1:");
        preco_peca1 = sc.nextDouble();

        System.out.println("Digite o código da peça 2:");
        codigo_peca2 = sc.nextInt();
        System.out.println("Digite a quantidade de peças da peça 2:");
        numero_peca2 = sc.nextInt();
        System.out.println("Digite o valor da peça 2:");
        preco_peca2 = sc.nextDouble();

        valor_pagar = (preco_peca1 * numero_peca1) + (preco_peca2 * numero_peca2);
        System.out.printf("Valor a pagar: %.2f",valor_pagar);



    }


}

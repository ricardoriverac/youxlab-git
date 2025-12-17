package curso_completo_java.sessao_05.exercicios;

/*Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A
seguir, calcule e mostre o valor da conta a pagar.*/

import java.util.Scanner;

public class exercicio_iniciante05 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Qual o seu pedido?: ");
        System.out.println("[1] Cachorro quente → R$ 4,00\n" +
                "[2] X - salada → R$ 4,50  \n" +
                "[3] X - bacon → R$ 5,00 \n" +
                "[4] Torrada simples → R$ 2,00 \n" +
                "[5] Cachorro quente → R$ 1,50: \n");

        int escolha = sc.nextInt();

        System.out.println("Quantos pedidos você fez? ");
        int pedidos = sc.nextInt();

        double valor_pagar;

        if (escolha == 1) {
            valor_pagar = pedidos * 4.0;
        }
        else if (escolha == 2) {
            valor_pagar = pedidos * 4.5;
        }
        else if (escolha == 3) {
            valor_pagar = pedidos * 5.0;
        }
        else if (escolha == 4) {
            valor_pagar = pedidos * 2.0;
        }
        else {
            valor_pagar = pedidos * 1.5;
        }

        System.out.printf("Total a pagar: R$ %.2f%n", valor_pagar);

        sc.close();

        }





    }

package Estrutura_condicional05.pratica;

/*AULA 43 - Sintaxe opcional - operadores de atribuição cumulativa */

/* Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100
minutos de telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00.
Fazer um programa para ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.*/

import java.util.Scanner;
import java.util.Locale;

public class pratica_exemplo03 {

   public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int minutos = sc.nextInt();

        double conta = 50.0;

        if (minutos > 100) {
            conta = conta + (minutos - 100) * 2.0;
        }

        System.out.printf("Valor da conta: R$ %.2f%n", conta);

        sc.close();

    }
}

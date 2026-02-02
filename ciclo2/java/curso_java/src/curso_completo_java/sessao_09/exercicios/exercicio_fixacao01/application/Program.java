package curso_completo_java.sessao_09.exercicios.exercicio_fixacao01.application;

import curso_completo_java.sessao_09.exercicios.exercicio_fixacao01.etities.Account;

import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Account account;

        System.out.println("Digite o número da conta: ");
        int numero = sc.nextInt();

        System.out.println("Digite o nome do titular da conta: ");
        sc.nextLine();
        String titular = sc.nextLine();

        System.out.println("Existe algum depósito inicial (s/n)?: ");
        char resposta = sc.next().charAt(0);

        if (resposta == 's') {
            System.out.println("Insira o valor do depósito inicial: R$ ");
            double deposito_inicial = sc.nextDouble();
            account = new Account(numero, titular, deposito_inicial);
        }
        else {
            account = new Account(numero, titular);
        }

        System.out.println();
        System.out.println("→ Dados da conta ←");
        System.out.println(account);
        System.out.println();

        System.out.print("insira um valor de saque: ");
        double saque = sc.nextDouble();
        account.withdraw(saque);
        System.out.println("Dados da conta atualizados:");
        System.out.println(account);


        sc.close();
    }
}

package Aula_89.Exercicio_Fixacao;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Objetos
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Conta cnt = new Conta();

        //Variavel
        double valorDouble;

        // Insercão do Número da conta
        System.out.print("Digite número da conta: ");
        int valorInt = sc.nextInt();
        if (valorInt != cnt.getNumero()) {
            System.out.println("Número da conta invalida!");
            return;
        }

        //Inserção do Nome do Titular
        System.out.print("Digite o titular da conta: ");
        String variavelAleatoria = sc.nextLine();
        String valorString = sc.nextLine();
        cnt.setTitular(valorString);

        //Pergunta se o cliente deseja depositar
        System.out.print("Há um depósito inicial (s/n): ");
        String opcao = sc.next();
        if (opcao.equals("S") || opcao.equals("s")) {
            System.out.print("Digite o valor do depósito: ");
            valorDouble = sc.nextDouble();
            cnt.deposito(valorDouble);
        }

        //Mostra as informações anteriores na tela
        System.out.println(" ");
        System.out.println("Dados da conta: ");
        System.out.println("Conta: "
                            + cnt.getNumero()
                            + ", Titular: "
                            + cnt.getTitular()
                            + ", saldo: "
                            + cnt.getSaldo());

        //Inserção do 2º deposito
        System.out.println(" ");
        System.out.print("Digite o valor do depósito: ");
        valorDouble = sc.nextDouble();
        cnt.deposito(valorDouble);
        System.out.println("Conta: "
                + cnt.getNumero()
                + ", Titular: "
                + cnt.getTitular()
                + ", saldo: "
                + cnt.getSaldo());

        System.out.println(" ");
        System.out.print("Digite o valor de saque: ");
        double valor2 = sc.nextDouble();





    }
}

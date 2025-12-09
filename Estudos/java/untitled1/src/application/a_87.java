package application;

import application.entities.AgenciaBancaria;

import java.util.Locale;
import java.util.Scanner;

public class a_87 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc  = new Scanner(System.in);
        AgenciaBancaria ag;
        int numConta;
        double depositoInicial, deposito, saldo = 0, saque;
        System.out.println("Caro usuário, para fazermos seu cadastro insira os dados abaixo: ");
        System.out.print("Caro usuário, escolha o número da sua conta: ");
        numConta = sc.nextInt();
        sc.nextLine();
        System.out.print("Caro usuário, qual o seu nome completo? ");
        String nome = sc.nextLine();
        System.out.print("Caro usuário, você está a um passo de criar sua conta! Você deseja fazer depósito inicial?[S/N] ");
        String confirmarDeposito = sc.nextLine();
        while (!confirmarDeposito.equals("S") && !confirmarDeposito.equals("N")){
            System.out.print("Caro usuário, por favor insira uma resposta válida! [S/N]");
            System.out.print("Caro usuário, você está a um passo de criar sua conta! Você deseja fazer depósito inicial?[S/N] ");
            confirmarDeposito = sc.nextLine();
        }
        if (confirmarDeposito.equals("N") || confirmarDeposito.equals("S")){
            if (confirmarDeposito.equals("N")){
                ag = new AgenciaBancaria(numConta, nome);
                System.out.print("Conta bancária cadastrada! ");
            }
            else{
                System.out.print("Caro usuário, qual o valor de seu depósito inicial? ");
                depositoInicial = sc.nextDouble();
                 ag = new AgenciaBancaria(numConta, nome, depositoInicial);
                ag.saldoInicial(depositoInicial);

            }
            System.out.println("Account data: " + ag.toString());
            System.out.print("Caro usuário, quantos reais você deseja depositar em sua conta? ");
            deposito = sc.nextDouble();
            ag.addSaldoo(saldo+=deposito);
            System.out.println("Updated data: " + ag.toString());
            System.out.print("Caro usuário, quantos reais você deseja sacar?");
            saque = sc.nextDouble();
            ag.removerSaldo(saldo-=saque);
            System.out.print("Updated data: " + ag.toString());


        }
    }
}

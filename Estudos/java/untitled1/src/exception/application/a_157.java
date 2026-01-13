package exception.application;

import exception.entities.Conta;
import exception.exception.InsufficientBalanceException;
import exception.exception.WithdrawalLimitExceededException;

import java.util.Locale;
import java.util.Scanner;

public class a_157 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Caro usuário, por favor informe o número da conta: ");
            Integer numeroConta = sc.nextInt();
            System.out.print("Caro usuário, por favor informe o nome do titular da conta: ");
            String titular = sc.next();
            System.out.print("Caro usuário, por favor informe o saldo da conta: ");
            Double saldo = sc.nextDouble();
            System.out.print("Caro usuário, por favor informe o limite de saque da conta: ");
            Double limiteSaque = sc.nextDouble();
            Conta conta = new Conta(numeroConta, titular, saldo, limiteSaque);

            System.out.print("Caro usuário, por favor insira qual o valor do saque: ");
            Double saque = sc.nextDouble();
            conta.saque(saque);
            System.out.print(conta);
        }
        catch (InsufficientBalanceException e){
            System.out.print("Erro de saque (Saldo): " + e.getMessage());
        }
        catch (WithdrawalLimitExceededException e){
            System.out.print("Erro de saque(Limite): " + e.getMessage());
        }
        catch (RuntimeException e){
            System.out.print("Erro inesperado!");
        }
   }
}

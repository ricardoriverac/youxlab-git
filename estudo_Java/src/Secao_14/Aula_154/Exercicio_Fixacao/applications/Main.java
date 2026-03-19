package Secao_14.Aula_154.Exercicio_Fixacao.applications;

import Secao_14.Aula_154.Exercicio_Fixacao.entities.ContaBancaria;
import Secao_14.Aula_154.Exercicio_Fixacao.model_exception.SaldoInsuficienteException;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Digite o valor do seu saldo: ");
            double saldo = sc.nextInt();

            ContaBancaria cb = new ContaBancaria(saldo);

            System.out.println("Saldo da conta: " + cb.getSaldo());

            System.out.print("\nDigite o valor do saque: ");
            double saque = sc.nextDouble();


            cb.sacar(saque);

            System.out.println(cb);
        }
        catch (SaldoInsuficienteException e) {
            System.out.println(e.getMessage());
        }
        catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}

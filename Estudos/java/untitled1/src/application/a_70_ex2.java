package application;

import application.entities.Funcionarios;

import java.util.Locale;
import java.util.Scanner;

public class a_70_ex2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Funcionarios funcionario;

        funcionario = new Funcionarios();

        System.out.print("Caro usuário, qual o nome do funcionário? ");
        funcionario.nome = sc.nextLine();
        System.out.print("Caro usuário, qual o seu salário bruto? ");
        funcionario.salarioBruto = sc.nextDouble();
        System.out.print("Caro usuário, qual a taxa de imposto descontada de seu salário? ");
        funcionario.imposto = sc.nextDouble();
        System.out.println("Funcionário: " + funcionario);

        System.out.print("Caro usuário, quanto em porcentagem o funcionário ganhará de aumento? ");
        double porcentagem = sc.nextDouble();
        funcionario.aumentarSalario(porcentagem);
        System.out.print(" Dados do funcionário atualizados: " + funcionario);

        sc.close();
    }
}

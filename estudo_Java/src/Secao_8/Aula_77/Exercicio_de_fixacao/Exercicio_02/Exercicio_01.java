package Aula_77.Exercicio_de_fixacao.Exercicio_02;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_01 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Calculo_Salarial salario = new Calculo_Salarial();

        System.out.print("Nome: ");
        salario.nome = sc.nextLine();

        System.out.print("Salário bruto: ");
        salario.salarioBruto = sc.nextDouble();

        System.out.print("Imposto: ");
        salario.imposto = sc.nextDouble();
;
        System.out.printf(salario.toString() + "%n");

        System.out.print("Which percentage to increase salary?");
        double porcentagem = sc.nextDouble();
        salario.AumentarSalario(porcentagem);

        System.out.printf(salario.toString());
    }
}

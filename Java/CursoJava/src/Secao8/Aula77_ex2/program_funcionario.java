package Secao8.Aula77_ex2;

import java.util.Locale;
import java.util.Scanner;

public class program_funcionario {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        funcionario Funcionario = new funcionario();
        System.out.print("Name: ");
        Funcionario.name = sc.nextLine();
        System.out.print("Gross Salary: ");
        Funcionario.GrossSalary = sc.nextDouble();
        System.out.print("Tax: ");
        Funcionario.Tax = sc.nextDouble();
        System.out.println("Employee: "+ Funcionario);


        System.out.print("Which percentage to increase salary? ");
        double GrossSalary = sc.nextDouble();
        Funcionario.increaseSalary(GrossSalary);

        System.out.println("Update data: "+ Funcionario);



        sc.close();
    }

}

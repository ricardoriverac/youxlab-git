package Listas.Exercicio.application;

import Listas.Exercicio.entities.Employee;

import java.security.PublicKey;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Employee> funcionarios = new ArrayList<>();
        System.out.print("How many employees will be registered? ");
        int quantidadeRegistros = sc.nextInt();

        int id;
        String nome;
        double salario;
        Employee employee = new Employee();

        for (int i = 0; i < quantidadeRegistros; i++) {
            System.out.println();
            System.out.println("Employee #" + (i+1) + ":");
            System.out.print("Id: ");
            id = (sc.nextInt());
            while (hasId(funcionarios, id)) {
                System.out.println("Id already taken!");
                System.out.print("New id: ");
                id = sc.nextInt();
            }

            System.out.print("Name: ");
            sc.nextLine();
            nome = (sc.next());
            System.out.print("Salary: ");
            salario = (sc.nextDouble());

            employee = new Employee(id, nome, salario);
            funcionarios.add(employee);

        }


        System.out.println();
        System.out.print("Enter the employee id that will have salary increase: ");
        int idsalary = sc.nextInt();
        Integer posicao = position(funcionarios, idsalary);

        if (posicao == null) {
            System.out.println("This id does not exist!");
        }

        else {
            System.out.print("Enter the percentage: ");
            double percent = sc.nextDouble();
            funcionarios.get(posicao).increaseSalary(percent);
        }

        System.out.println();
        System.out.println("List of employees:");
        for (Employee emp : funcionarios) {
            System.out.println(emp);
        }

        sc.close();
    }

    public static Integer position(List<Employee> list, int id){
        for (int i = 0; i < list.size(); i++) {
            if(list.get(i).getId() == id) {
                return i;
            }
        }

        return null;
    }

    public static boolean hasId(List<Employee> list, int id) {
        Employee emp = list.stream().filter(x -> x.getId() == id).findFirst().orElse(null);
        return emp != null;
    }
}

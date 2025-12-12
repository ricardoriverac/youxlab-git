package Programacao_Orientada_Objetos.Exercicios.Employee;

public class Employee {
    public String name;
    public double grossSalary;
    public double tax;

    public double netSalary() {
        return grossSalary - tax;
    }

    public void increaseSalary(double porcentage) {
        this.grossSalary +=  (this.grossSalary * (porcentage / 100));
    }
}

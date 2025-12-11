package Programacao_Orientada_Objetos.Exercicios.Employee;

public class employee {
    public static String name;
    public double grossSalary;
    public static double tax;

    public static double netSalary() {
        return grossSalary - tax;
    }

    public void increaseSalary(double porcentage) {
        this.grossSalary *= (porcentage / 100);
    }
}

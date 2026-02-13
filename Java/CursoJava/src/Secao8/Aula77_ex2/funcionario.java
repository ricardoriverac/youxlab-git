package Secao8.Aula77_ex2;

public class funcionario {

    public String name;
    public double GrossSalary;
    public double Tax;

    public double netSalary() {
        return GrossSalary - Tax;
    }
    public void increaseSalary(double GrossSalary) {
        this.GrossSalary += this.GrossSalary * (GrossSalary / 100.0);
    }
    public String toString() {
        return
                String.format(name)
                +String.format(", %.2f\n",netSalary());

    }
}

package secao_08.exercicio_2.entities;

public class Employee {
    public String name;
    public double grossSalary;
    public double tax;

    public double netSalary(){
        return grossSalary - tax;
    }

    public void increaseSalary(double percentage){
        this.grossSalary = this.grossSalary + (this.grossSalary * (percentage / 100));
    }

    public String toString(){
        return "Employee:"
                + "\nName: " +  name
                + "\nGross Salary: " + grossSalary
                + "\nNet Salary: " + netSalary();
    }
}

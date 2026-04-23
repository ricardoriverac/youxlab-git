package Secao_16.Aula_182.Interface_Comparable.entities;

import org.jetbrains.annotations.NotNull;

public class Employee implements Comparable<Employee> {

    private String name;
    private Double salary;

    public Employee(String name, Double salary) {
        this.name = name;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    @Override
    public int compareTo(@NotNull Employee other) {
        return this.name.compareTo(other.getName());
    }
}
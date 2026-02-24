package Secao12.aula130;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

public class Woker {
    private String name;
    private workLevel level;
    private Double baseSalary;

    private Departament department;
    private List<HoursContract> contracts = new ArrayList<>();

    public Woker() {
    }

    public Woker(String name, workLevel level, Double baseSalary, Departament department) {
        this.name = name;
        this.level = level;
        this.baseSalary = baseSalary;
        this.department = department;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workLevel getLevel() {
        return level;
    }

    public void setLevel(workLevel level) {
        this.level = level;
    }

    public Double getBaseSalary() {
        return baseSalary;
    }

    public void setBaseSalary(Double baseSalary) {
        this.baseSalary = baseSalary;
    }

    public Departament getDepartment() {
        return department;
    }

    public void setDepartment(Departament department) {
        this.department = department;
    }

    public List<HoursContract> getContracts() {
        return contracts;
    }

    public void addContract(HoursContract contract) {
        contracts.add(contract);
    }

    public void removeContract(HoursContract contract) {
        contracts.remove(contract);
    }

    public double income(int year, int month) {
        double sum = baseSalary;
        Calendar cal = Calendar.getInstance();
        for (HoursContract c : contracts) {
            cal.setTime(c.getDate());
            int c_year = cal.get(Calendar.YEAR);
            int c_month = 1 + cal.get(Calendar.MONTH);
            if (year == c_year && month == c_month) {
                sum += c.totalValue();
            }
        }
        return sum;
    }
}

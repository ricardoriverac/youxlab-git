package secao12_Enumerates.exercicioResolvido1;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

public class worker {
    // composição "tem-um"
    private String name;
    private enum1 level;
    private Double baseSalary;

    private mets1 department;
    //composição tem-muitos
    private List<hourContract> contracts = new ArrayList<>();

    public worker(){

    }
    public worker(String name, enum1 level, Double baseSalary, mets1 department){
        this.name = name;
        this.level = level;

    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public enum1 getLevel() {
        return level;
    }

    public void setLevel(enum1 level) {
        this.level = level;
    }

    public Double getBaseSalary() {
        return baseSalary;
    }

    public void setBaseSalary(Double baseSalary) {
        this.baseSalary = baseSalary;
    }

    public mets1 getDepartment() {
        return department;
    }

    public void setDepartment(mets1 department) {
        this.department = department;
    }

    public List<hourContract> getContracts() {
        return contracts;
    }
    public void addContract(hourContract contract) {
        contracts.add(contract);
    }
    public void removeContract(hourContract contract){
        contracts.remove(contract);
    }
    private double income(int ywear, int month){
        double sum = baseSalary;
        Calendar cal = Calendar.getInstance();
        for (hourContract c: contracts) {
            cal.setTime(c.getDate());
            int c_year = cal.get(Calendar.YEAR);
            int c_month = 1 + cal.get(Calendar.MONTH);
            if (c_year == c_year && month == c_month) {
                sum += c.totalValue();
            }
        }
        return sum;
    }

}

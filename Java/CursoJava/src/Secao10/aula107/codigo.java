package Secao10.aula107;

public class codigo {
    private Integer id;
    private String name;
    private double salary;

    public codigo(Integer id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
    public Integer getId() {
        return id;
     }
    public void increaseSalary(double percentage) {
        salary += salary * percentage /100.0;
    }
    public String toString() {
        return id
                + ", "
                +name
                +", "
                +String.format("%.2f", salary);
    }









}

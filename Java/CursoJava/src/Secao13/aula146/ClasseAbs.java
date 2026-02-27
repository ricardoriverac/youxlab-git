package Secao13.aula146;

public  abstract class ClasseAbs {
    private String name;
    private Double renda;

    public ClasseAbs(String name, Double renda) {
        this.name = name;
        this.renda = renda;
    }

    public String getName() {
        return name;
    }
    public Double getRenda() {
        return renda;
    }
    public abstract double tax();
}


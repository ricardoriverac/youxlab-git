package Secao_13.Aula_144.Classes_Abstratas.entities;

public class Gerente extends Funcionario{

    private Double bonus;

    public Gerente() {
        super();
    }

    public Gerente(String nome, Double salarioBase, Double bonus) {
        super(nome, salarioBase);
        this.bonus = bonus;
    }

    public Double getBonus() {
        return bonus;
    }

    public void setBonus(Double bonus) {
        this.bonus = bonus;
    }

    @Override
    double calcularSalario() {
        return super.salarioBase + bonus;
    }
}

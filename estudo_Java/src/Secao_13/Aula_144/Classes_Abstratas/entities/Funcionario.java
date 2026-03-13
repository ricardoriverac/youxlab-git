package Secao_13.Aula_144.Classes_Abstratas.entities;

public abstract class Funcionario {

    protected String nome;
    protected Double salarioBase;

    public Funcionario() {}

    public Funcionario(String nome, Double salarioBase) {
        this.nome = nome;
        this.salarioBase = salarioBase;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getSalarioBase() {
        return salarioBase;
    }

    abstract double calcularSalario();

    public void exibirDados() {
        System.out.println("Nome: " + nome);
        System.out.println("Salário Base: " + salarioBase);
        System.out.println("Salário Final: " + calcularSalario());
        System.out.println("---------------------------");
    }

}

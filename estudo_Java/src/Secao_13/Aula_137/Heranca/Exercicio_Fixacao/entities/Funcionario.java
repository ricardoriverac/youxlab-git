package Secao_13.Aula_137.Heranca.Exercicio_Fixacao.entities;

public class Funcionario {

    private String nome;
    protected Double salario;

    public Funcionario() {}

    public Funcionario(String nome, Double salario) {
        this.nome = nome;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getSalario() {
        return salario;
    }

    public double calculaBonus() {
        return this.salario * 0.10;
    }

    public String exibirDados() {
        return "Nome: " + this.nome
                + ", Salário: " + this.salario
                + ", Bônus: " + calculaBonus();
    }
}

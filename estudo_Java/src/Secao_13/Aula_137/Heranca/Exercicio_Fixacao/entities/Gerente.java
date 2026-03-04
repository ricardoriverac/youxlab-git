package Secao_13.Aula_137.Heranca.Exercicio_Fixacao.entities;

public class Gerente extends Funcionario{

    public Gerente() {
    }

    public Gerente(String nome, Double salario) {
        super(nome, salario);
    }

    @Override
    public double calculaBonus() {
        return getSalario() * 0.20;
    }

}

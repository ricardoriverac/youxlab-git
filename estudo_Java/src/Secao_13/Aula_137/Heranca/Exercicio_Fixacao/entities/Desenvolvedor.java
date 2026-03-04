package Secao_13.Aula_137.Heranca.Exercicio_Fixacao.entities;

public class Desenvolvedor extends Funcionario{

    public Desenvolvedor() {
    }

    public Desenvolvedor(String nome, Double salario) {
        super(nome, salario);
    }

    @Override
    public double calculaBonus() {
        return getSalario() * 0.15;
    }
}

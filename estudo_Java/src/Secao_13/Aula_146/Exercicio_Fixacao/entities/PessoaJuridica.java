package Secao_13.Aula_146.Exercicio_Fixacao.entities;

public class PessoaJuridica extends Pessoa{

    private Integer numreroFuncionario;

    public PessoaJuridica() {
        super();
    }

    public PessoaJuridica(Double rendaAnual, String nome, Integer numreroFuncionario) {
        super(rendaAnual, nome);
        this.numreroFuncionario = numreroFuncionario;
    }

    @Override
    double calculoImposto() {
        double valorTotal = 0;
        if (numreroFuncionario < 10) {
            valorTotal = getRendaAnual() * 0.16;
        }
        else {
            valorTotal = getRendaAnual() * 0.14;
        }
        return valorTotal;
    }
}

package Secao_13.Aula_146.Exercicio_Fixacao.entities;

public class PessoaFisica extends Pessoa{

    private Double gastoSaude;

    public PessoaFisica() {
        super();
    }

    public PessoaFisica(Double rendaAnual, String nome, Double gastoSaude) {
        super(rendaAnual, nome);
        this.gastoSaude = gastoSaude;
    }

    public Double getGastoSaude() {
        return gastoSaude;
    }

    public void setGastoSaude(Double gastoSaude) {
        this.gastoSaude = gastoSaude;
    }

    @Override
    double calculoImposto() {
        double valorTotal = 0;
        if (getRendaAnual() < 20000.00){
            valorTotal = (getRendaAnual() * 0.15) - (gastoSaude * 0.50);
        }
        else if (getRendaAnual() > 20000.00) {
            valorTotal = (getRendaAnual() * 0.25) - (gastoSaude * 0.50);
        }
        return valorTotal;
    }


}

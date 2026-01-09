package application.entities;

public class PessoaFisica extends Contribuinte{
    private Double despesaSaude;

    public PessoaFisica() {
        super();
    }




    public PessoaFisica(String nome, Double rendaAnual, Double despesaSaude) {
        super(nome, rendaAnual);
        this.despesaSaude = despesaSaude;
    }

    public Double getDespesaSaude() {
        return despesaSaude;
    }

    public void setDespesaSaude(Double despesaSaude) {
        this.despesaSaude = despesaSaude;
    }

    @Override
    public Double taxa() {
        if (getRendaAnual() < 20000.00) {
            return getRendaAnual() * 0.15 - despesaSaude * 0.5;
        }
        else {
            return getRendaAnual() * 0.25 - despesaSaude * 0.5;
        }
    }

    @Override
    public String toString() {
        return getNome() + ":" + " $ " + taxa() + "\n";
    }
}

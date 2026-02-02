package curso_completo_java.sessao_13.exercicios.exercicio03.entities;

public class PessoaFisica extends Contribuinte{

    private Double gastosSaude;

    public PessoaFisica(String nome, Double rendaAnual, Double gastosSaude) {
        super(nome, rendaAnual);
        this.gastosSaude = gastosSaude;
    }

    @Override
    public Double imposto() {
        double impostoBase;

        if (getRendaAnual() < 20000.0) {
            impostoBase = getRendaAnual() * 0.15;
        } else {
            impostoBase = getRendaAnual() * 0.25;
        }

        impostoBase -= gastosSaude * 0.5;

        return impostoBase;
    }
}

package Secao_13.Aula_139.Exercicio.Sobreposicao.entities;

public class Boleto extends Pagamento{

    public Boleto() {
    }

    public Boleto(double valor) {
        super(valor);
    }

    @Override
    public double calcularValorFinal() {
        return getValor() * 0.90;
    }
}

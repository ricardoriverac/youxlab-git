package Secao_13.Aula_137.Sobreposicao.Exercicio.entities;

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

package Secao_13.Aula_139.Exercicio.Sobreposicao.entities;

public class CartaoCredito extends Pagamento{

    public CartaoCredito() {
    }

    public CartaoCredito(double valor) {
        super(valor);
    }

    @Override
    public double calcularValorFinal() {
        return getValor() * 1.05;
    }
}

package Secao_13.Aula_139.Exercicio.Sobreposicao.entities;

public class Pix extends Pagamento {

    public Pix() {
    }

    public Pix(double valor) {
        super(valor);
    }

    @Override
    public double calcularValorFinal() {
        return getValor() * 0.95;
    }
}

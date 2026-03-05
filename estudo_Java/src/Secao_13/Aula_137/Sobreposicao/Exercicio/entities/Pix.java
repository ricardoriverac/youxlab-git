package Secao_13.Aula_137.Sobreposicao.Exercicio.entities;

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

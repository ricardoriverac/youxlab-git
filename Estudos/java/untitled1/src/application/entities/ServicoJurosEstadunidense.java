package application.entities;

public class ServicoJurosEstadunidense implements ServicoJuros{
    private Double taxaJuros;

    public ServicoJurosEstadunidense(Double taxaJuros) {
        this.taxaJuros = taxaJuros;
    }


    @Override
    public double getTaxajuros() {
        return taxaJuros;
    }
}

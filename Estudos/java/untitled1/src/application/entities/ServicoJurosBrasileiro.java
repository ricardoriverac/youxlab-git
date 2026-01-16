package application.entities;

public class ServicoJurosBrasileiro implements ServicoJuros {
    private Double taxaJuros;


    public ServicoJurosBrasileiro(Double taxaJuros) {
        this.taxaJuros = taxaJuros;
    }


    @Override
    public double getTaxajuros() {
        return taxaJuros;
    }
}

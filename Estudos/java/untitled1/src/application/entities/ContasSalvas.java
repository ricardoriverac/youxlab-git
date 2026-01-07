package application.entities;

public class ContasSalvas extends Conta{
    private Double jurosTaxa;

    public ContasSalvas() {
        super();
    }

    public ContasSalvas(Integer numero, String titular, Double saldo, Double jurosTaxa) {
        super(numero, titular, saldo);
        this.jurosTaxa = jurosTaxa;
    }

    public Double getJurosTaxa(){
        return jurosTaxa;
    }

    public void setJurosTaxa(Double jurosTaxa) {
        this.jurosTaxa = jurosTaxa;
    }

    public void atualizarSaldo(){
        saldo += saldo * jurosTaxa;
    }
}

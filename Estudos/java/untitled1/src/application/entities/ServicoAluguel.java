package application.entities;

public class ServicoAluguel {
    private Double precoPorDia;
    private Double precoPorHora;

    private ImpostoBrasilServico impostoServico;


    public ServicoAluguel(Double precoPorDia, Double precoPorHora, ImpostoBrasilServico impostoServico) {
        this.precoPorDia = precoPorDia;
        this.precoPorHora = precoPorHora;
        this.impostoServico = impostoServico;
    }

    public void processoFatura(AluguelCarro aluguelCarro){
        long tempo1 = aluguelCarro.getInicio().getTime();
        long tempo2 = aluguelCarro.getFim().getTime();
        double horas = (double) (tempo2-tempo1)/1000/60/60;

        double pagamentoBasico;

        if(horas <= 12.0){
            pagamentoBasico = precoPorHora * Math.ceil(horas);
        }
        else {
            pagamentoBasico = precoPorDia * Math.ceil(horas);
        }

        double imposto = impostoServico.imposto(pagamentoBasico);

        aluguelCarro.setFatura(new Fatura(pagamentoBasico, imposto));
    }
}

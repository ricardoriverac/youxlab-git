package Secao16.aula172;

import java.time.LocalDateTime;

public class carRental {
    private LocalDateTime start;
    private LocalDateTime finish;

    private Veiculo veiculo;
    private Invoice invoice;

    public carRental(){
    }

    public carRental(LocalDateTime start, LocalDateTime finish, Veiculo veiculo) {
        this.start = start;
        this.finish = finish;
        this.veiculo = veiculo;
    }

    public LocalDateTime getStart() {
        return start;
    }
    public LocalDateTime getFinish() {
        return finish;
    }
    public Veiculo getVeiculo() {
        return veiculo;
    }
    public Invoice getInvoice() {
        return invoice;
    }
    public void setInvoice(Invoice invoice) {
        this.invoice = invoice;
    }
}

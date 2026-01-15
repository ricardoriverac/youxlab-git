package application.entities;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

public class Parcelas {
    private LocalDate dataParcela;
    private Double valorParcela;

    public Parcelas(LocalDate dataParcela, Double valorParcela) {
        this.dataParcela = dataParcela;
        this.valorParcela = valorParcela;
    }

    public LocalDate getDataParcela() {
        return dataParcela;
    }

    public void setDataParcela(LocalDate dataParcela) {
        this.dataParcela = dataParcela;
    }

    public Double getValorParcela() {
        return valorParcela;
    }

    public void setValorParcela(Double valorParcela) {
        this.valorParcela = valorParcela;
    }

    @Override
    public String toString() {
        return dataParcela + ", " + valorParcela;
    }
}

package application.entities;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Contrato {
    private Integer numero;
    private LocalDate dataContrato;
    private Double valorTotal;
    List<Parcelas> parcelas = new ArrayList<>();

    public Contrato() {
    }

    public Contrato(Integer numero, LocalDate dataContrato, Double valorTotal) {
        this.numero = numero;
        this.dataContrato = dataContrato;
        this.valorTotal = valorTotal;
    }

    public Integer getNumero() {
        return numero;
    }

    public LocalDate getDataContrato() {
        return dataContrato;
    }

    public Double getValorTotal() {
        return valorTotal;
    }

    public List<Parcelas> getParcelas() {
        return parcelas;
    }

    public void setParcelas(List<Parcelas> parcelas) {
        this.parcelas = parcelas;
    }
}

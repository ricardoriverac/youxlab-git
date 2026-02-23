package Secao_12.Aula_129.Exercicio_Parte_1;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Contrato {

    DateTimeFormatter fmt1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");

    private int ducaoHoras;
    private double valorHoras;
    private LocalDate data;

    public Contrato(int ducaoHoras, double valorHoras, LocalDate data) {
        this.ducaoHoras = ducaoHoras;
        this.valorHoras = valorHoras;
        this.data = data;
    }

    public int getDucaoHoras() {
        return ducaoHoras;
    }

    public double getValorHoras() {
        return valorHoras;
    }

    public LocalDate getData() {
        return data;
    }

    @Override
    public String toString() {
        return "Class{" +
                "ducaoHoras=" + ducaoHoras +
                ", valorHoras=" + valorHoras +
                ", data=" + data.format(fmt1) +
                '}';
    }
}

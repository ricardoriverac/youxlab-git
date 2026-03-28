package Secao_16.Aula_172.Interface.Interface_1.entites;

import Secao_16.Aula_172.Interface.Interface_1.interfaces.Forma;

public class Quadrado implements Forma {

    private Double lado;

    public Quadrado() {}

    public Quadrado(Double lado) {
        this.lado = lado;
    }

    public Double getLado() {
        return lado;
    }

    public void setLado(Double lado) {
        this.lado = lado;
    }

    @Override
    public double calcularArea() {
        return lado * lado;
    }
}

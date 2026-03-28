package Secao_16.Aula_172.Interface.Interface_1.entites;

import Secao_16.Aula_172.Interface.Interface_1.interfaces.Forma;

public class Circulo implements Forma {

    private Double raio;

    public Circulo() {}

    public Circulo(Double raio) {
        this.raio = raio;
    }

    public Double getRaio() {
        return raio;
    }

    public void setRaio(Double raio) {
        this.raio = raio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * (raio * raio);
    }
}

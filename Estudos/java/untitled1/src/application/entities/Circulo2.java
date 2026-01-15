package application.entities;

public class Circulo2 extends FormaAbstrata{
    private Double raio;

    public Circulo2(Color color, Double raio) {
        super(color);
        this.raio = raio;
    }

    public Double getRaio() {
        return raio;
    }

    public void setRaio(Double raio) {
        this.raio = raio;
    }

    @Override
    public double area(){
        return Math.PI * Math.pow(raio, 2);
    }
}

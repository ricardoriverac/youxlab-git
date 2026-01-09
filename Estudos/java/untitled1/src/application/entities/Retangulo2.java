package application.entities;

public class Retangulo2 extends Forma {
    private Double altura;
    private Double largura;

    public Retangulo2() {
        super();
    }


    public Retangulo2(Double altura, Double largura, Color color) {
        super(color);
        this.altura = altura;
        this.largura = largura;
    }

    public Double getAltura() {
        return altura;
    }

    public void setAltura(Double altura) {
        this.altura = altura;
    }

    public Double getLargura() {
        return largura;
    }

    public void setLargura(Double largura) {
        this.largura = largura;
    }

    @Override
    public final Double area() {
        return largura * altura;
    }
}

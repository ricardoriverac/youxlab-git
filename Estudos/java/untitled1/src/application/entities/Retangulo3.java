package application.entities;

public class Retangulo3 extends FormaAbstrata {
    private Double altura;
    private Double largura;

    public Retangulo3(Color color, Double altura, Double largura) {
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
    public double area(){
        return largura * altura;
    }
}

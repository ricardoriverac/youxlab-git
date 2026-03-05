package Secao_13.Aula_140.Classe_metodos_final.entities;

public class Veiculo {

    private String marca;
    private String modelo;
    private Double velocidadeAtual;

    public Veiculo() {}

    public Veiculo(String marca, String modelo, Double velocidadeAtual) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidadeAtual = velocidadeAtual;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public Double getVelocidadeAtual() {
        return velocidadeAtual;
    }


    public void acelerar(double velocidadeAtual) {
        this.velocidadeAtual += velocidadeAtual;
    }

    public final String exibirInformacoes() {
        return "Marca: " + this.marca
                + " Modelo: " + this.modelo
                + " Velocidade Atual: " + this.velocidadeAtual;
    }
}

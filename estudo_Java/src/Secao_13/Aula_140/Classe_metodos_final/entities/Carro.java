package Secao_13.Aula_140.Classe_metodos_final.entities;

public class Carro extends Veiculo{

    public Carro() {
        super();
    }

    public Carro(String marca, String modelo, Double velocidadeAtual) {
        super(marca, modelo, velocidadeAtual);
    }

    public String ligarArCondicionado() {
        return "Ar-condicionado ligado! ";
    }

}

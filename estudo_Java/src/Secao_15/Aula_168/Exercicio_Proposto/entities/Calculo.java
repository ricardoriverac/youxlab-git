package Secao_15.Aula_168.Exercicio_Proposto.entities;

public class Calculo {

    private String nomeProduto;
    private Double precoTotal;
    private Integer quantidade;

    public Calculo() {}

    public Calculo(String nomeProduto, Double precoTotal, Integer quantidade) {
        this.nomeProduto = nomeProduto;
        this.precoTotal = precoTotal;
        this.quantidade = quantidade;
    }

    public String getNomeProduto() {
        return nomeProduto;
    }

    public void setNomeProduto(String nomeProduto) {
        this.nomeProduto = nomeProduto;
    }

    public Double getPrecoTotal() {
        return precoTotal;
    }

    public Integer getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(Integer quantidade) {
        this.quantidade = quantidade;
    }

    public Double precoTotal() {
        return precoTotal * quantidade;
    }
}

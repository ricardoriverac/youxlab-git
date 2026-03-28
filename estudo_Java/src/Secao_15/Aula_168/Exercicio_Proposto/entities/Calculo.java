package Secao_15.Aula_168.Exercicio_Proposto.entities;

public class Calculo {

    private String nomeProduto;
    private Double preco;
    private Integer quantidade;

    public Calculo() {}

    public Calculo(String nomeProduto, Double precoTotal, Integer quantidade) {
        this.nomeProduto = nomeProduto;
        this.preco = precoTotal;
        this.quantidade = quantidade;
    }

    public String getNomeProduto() {
        return nomeProduto;
    }

    public void setNomeProduto(String nomeProduto) {
        this.nomeProduto = nomeProduto;
    }

    public Double getPrecoTotal() {
        return preco;
    }

    public Integer getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(Integer quantidade) {
        this.quantidade = quantidade;
    }

    public Double precoTotal() {
        return preco * quantidade;
    }
}

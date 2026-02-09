package secao17_GenericSetMap.projetinhoSet;

public class Manga {
    private Integer quantity;
    private String nome;
    private Double price;

    public Manga(Integer quantity, String nome, Double price){
        this.nome = nome;
        this.price = price;
        this.quantity = quantity;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return super.toString();
    }
}

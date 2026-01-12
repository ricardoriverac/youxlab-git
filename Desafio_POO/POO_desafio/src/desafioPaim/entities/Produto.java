package desafioPaim.entities;

public class Produto {

    private int id;
    private String name;
    private double preco;

    public Produto(int id, String name, double preco) {
        this.id = id;
        this.name = name;
        this.preco = preco;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

}

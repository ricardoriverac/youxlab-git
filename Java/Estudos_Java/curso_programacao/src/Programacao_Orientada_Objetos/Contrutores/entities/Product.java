package Programacao_Orientada_Objetos.Contrutores.entities;

public class Product {
    public String name; // Valor padrao é null
    public double price; // Valor padrao é 0.0
    public int quantity; // Valor padrao é 0

    public Product(){
    }

    public Product(String name, double price, int quantity) { // construtor
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public Product(String name, double price) { // construtor
        this.name = name;
        this.price = price;
    }

    public double totalValueInStock() {
        return price * quantity;
    }

    public void addProducts(int quantity) {
        this.quantity += quantity; // soma a quantidade da classe Produto com a quantidade que foi dada como argumento
    }

    public void removeProducts(int quantity) {
        this.quantity -= quantity; // subtrai a quantidade da classe Produto com a quantidade que foi dada como argumento
    }

    public String toString() {
        return name
                + ", $ "
                + String.format("%.2f", price)
                + ", "
                + quantity
                + " units, Total: $ "
                + String.format("%.2f", totalValueInStock());
    }
}
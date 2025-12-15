package Programacao_Orientada_Objetos.Encapsulamento.entities;

public class Product {
    private String name; // Valor padrao é null
    private double price; // Valor padrao é 0.0
    private int quantity; // Valor padrao é 0

    // CONSTRUTORES
    public Product() {
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


    // ENCAPSULAMENTO
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQuantity() {
        return quantity;
    }

    // PRODUCT
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
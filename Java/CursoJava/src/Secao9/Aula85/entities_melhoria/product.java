package Secao9.Aula85.entities_melhoria;

public class product {
    public String name;
    public double price;
    public int quantity;

    public product() {

    }

    public product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
    public product(String name, double price) {
        this.name = name;
        this.price = price;
    }
    public double totalValuesInStock() {
        return price * quantity;
    }
    public void addProducts(int quantity) {
        this.quantity += quantity;
    }
    public void removeProducts(int quantity) {
        this.quantity -= quantity;
    }
    public String toString() {
        return name
                + ", $ "
                + String.format("%.2f", price)
                + ", "
                + quantity
                + " units, Total: $ "
                + String.format("%.2f", totalValuesInStock());}

}


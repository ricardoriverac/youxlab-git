package Secao12.aula133;

public class OrderItem {
    private Integer quantity;
    private double price;
    private Product product;

    public OrderItem(Integer quantity, double price, Product product){
        this.quantity = quantity;
        this.price = price;
        this.product = product;
    }
    public double subtotal() {
        return price * quantity;
    }
    public String toString(){
        return product.getName()
                +", $"
                +String.format("%.2f", price)
                +", Quantity: "
                +quantity
                +", Subtotal: $"
                +String.format("%.2f", subtotal());
    }
}

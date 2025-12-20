package secao_08.Product;

public class entities {

    public  String name;
    public double price;
    public int quantity;

    public double totalValueinSTock(){
        return price * quantity;
    }

    public void addProducts(int quantity) {
        this.quantity += quantity;
    }

    public void  removeProducts(int quantity){
        this.quantity -= quantity;
    }

    public String toString(){
        return name
                +", $"
                + String.format("%.2f", price)
                +","
                + quantity
                + "units, total: $"
                + totalValueinSTock();
    }

}


package Secao_12.Aula_133.entitis;

import Secao_12.Aula_133.Enum.OrderStatus;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Order {
    SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
    SimpleDateFormat sdf1 = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");

    private Date moment;
    private OrderStatus status;

    private Client client;
    List<OrderItem> items = new ArrayList<>();

    public Order() {}

    public Order(Date moment, OrderStatus status, Client client) {
        this.moment = moment;
        this.status = status;
        this.client = client;
    }

    public Date getMoment() {
        return moment;
    }

    public void setMoment(Date moment) {
        this.moment = moment;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public void setStatus(OrderStatus status) {
        this.status = status;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

    public List<OrderItem> getItems() {
        return items;
    }

    public void addItem(OrderItem item) {
        items.add(item);
   }

   public void removeItem(OrderItem item) {
        items.remove(item);
   }

   public Double total() {
       Double sum = 0.0;
       for (OrderItem c : items) {
           sum += c.subTotal();
       }

       return sum;
   }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\nORDER SUMMARY \n");
        sb.append("Order moment: " + this.sdf1.format(moment));
        sb.append("\nOrder status: " + this.status);
        sb.append("\nClient: " + client.getName() + " (" + (sdf.format(client.getBirthDate())) + ")" + " - " + client.getEmail());
        sb.append("\nOrder items: \n");
        for (OrderItem n : items){
            sb.append(n.getProduct().getName()
                    + ", "
                    + n.getProduct().getPrice()
                    + ", "
                    + "Quantity: "
                    + n.getQuantity()
                    + ", "
                    + "Subtotal: "
                    + n.subTotal()
                    + "\n");
        }
        sb.append("Total price: " + total());

        return sb.toString();
    }
}

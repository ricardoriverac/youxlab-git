package Secao12.aula133;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Order {
    private LocalDateTime moment;
    private OrderStatus status;
    private Cliente cliente;

    private List<OrderItem> items = new ArrayList<>();

    public Order(){
    }
    public Order(LocalDateTime moment, OrderStatus status, Cliente cliente){
      this.moment = moment;
      this.status = status;
      this.cliente = cliente;
    }
    public void addItem(OrderItem item){
        items.add(item);
    }
    public double total(){
        double sum = 0.0;
        for (OrderItem item : items){
            sum += item.subtotal();
        }
        return sum;
    }
    public String toString() {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");

        StringBuilder sb = new StringBuilder();
        sb.append("ORDER SUMMARY:\n");
        sb.append("Order moment: ").append(moment.format(fmt)).append("\n");
        sb.append("Order status: ").append(status).append("\n");
        sb.append("Cliente: ").append(cliente).append("\n");
        sb.append("Order items: \n");

        for (OrderItem item : items) {
            sb.append(item).append("\n");
        }
        sb.append("Total price: $").append(String.format("%.2f", total()));
        return sb.toString();
    }
}



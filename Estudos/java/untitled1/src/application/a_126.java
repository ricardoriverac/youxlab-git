package application;

import application.entities.OrderStatus;
import application.entities.Pedido;

import java.util.Date;

public class a_126 {
    public static void main(String[] args) {
        Pedido pedido = new Pedido(1000, new Date(), OrderStatus.PENDING_PAYMENT);

        System.out.println(pedido);
        OrderStatus os1 = OrderStatus.DELIVERED;
        OrderStatus os2 = OrderStatus.valueOf("DELIVERED");

        System.out.println(os1);
        System.out.println(os2);
    }
}


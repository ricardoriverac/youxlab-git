package Secao12.aula127.programa;

import Secao12.aula127.entities.Order;
import Secao12.aula127.entities_enums.OrderStatus;

import java.util.Date;

public class program {
    public static void main(String[] args) {

        Order order = new Order(1080, new Date(), OrderStatus.PENDING_PAYMENT);

        System.out.println(order);

        OrderStatus os1 = OrderStatus.DELIVERED;
        OrderStatus os2 = OrderStatus.valueOf("DELIVERED");


    }
}

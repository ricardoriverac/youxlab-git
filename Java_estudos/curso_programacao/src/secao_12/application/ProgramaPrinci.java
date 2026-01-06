package secao_12.application;

import secao_12.entities.Order;
import secao_12.entitiesenums.OrderStatus;

import java.util.Date;

public class ProgramaPrinci {
    static void main() {
        Order order = new Order(1080, new Date(), OrderStatus.PENDING_PAYMENT);

        System.out.println(order);
        OrderStatus os1 = OrderStatus.DEVILERED;
        OrderStatus os2 = OrderStatus.valueOf("DELIVERED");

        System.out.println(os1);
        System.out.println(os2);
    }
}

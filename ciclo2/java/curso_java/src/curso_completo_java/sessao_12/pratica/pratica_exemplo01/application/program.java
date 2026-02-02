package curso_completo_java.sessao_12.pratica.pratica_exemplo01.application;


import curso_completo_java.sessao_12.pratica.pratica_exemplo01.entities.enums.OrderStatus;
import curso_completo_java.sessao_12.pratica.pratica_exemplo01.etities.Order;

import java.util.Date;

public class program {

    public static void main(String[] args) {

        Order order = new Order(1080, new Date(), OrderStatus.PENDING_PAYMENT);

        System.out.println(order);

        OrderStatus os1 = OrderStatus.DEVILERED;
        OrderStatus os2 = OrderStatus.valueOf("DEVILERED");
    }

}

package Secao_12.Aula_127.Eumeracoes;

import java.util.Date;

public class Program {
    public static void main(String[] args) {

        Order order = new Order(1080, new Date(), OrderStatus.SHIPPED);
        Order order1 = new Order();
        Order order2 = new Order(new Date());


        order1.setId(123);
        order1.setStatus(OrderStatus.PENDING_PAYMET);

        System.out.println(order.getStatus());
        System.out.println(order1.toString());
        System.out.println(order2.toString());

        if (order.getStatus().toString().equals("SHIPPED")) {
            System.out.println("Aqui");
       }else {
            System.out.println("a baixo");
        }


        order2.setId(3435);
        order2.setStatus(OrderStatus.PROCESSING);
        System.out.println(order2.toString());

    }
}

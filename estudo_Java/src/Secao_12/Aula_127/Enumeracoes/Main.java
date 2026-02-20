package Aula_127.Enumeracoes;

import java.util.Date;
import java.util.OptionalDouble;

public class Main {
    public static void main(String[] args) {

        Class order = new Class(1080, new Date(), OrderStatus.PENDING_PAYMENT);

        System.out.println(order);

        OrderStatus os1 = OrderStatus.DELIVERED;
        OrderStatus os2 = OrderStatus.valueOf("DELIVERED");

        System.out.println(os1);
        System.out.println(os2);
    }
}

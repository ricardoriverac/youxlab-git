package EnumeracoesComposicao.Enumeracoes.application;

import EnumeracoesComposicao.Enumeracoes.entities.OrderStatus;
import EnumeracoesComposicao.Enumeracoes.entities.Pedido;

import java.util.Date;

public class Program {
    static void main() {

        Pedido pedido = new Pedido(1080, new Date(), OrderStatus.PENDING_PAYMENT);

        System.out.println(pedido);

        OrderStatus os1 = OrderStatus.DELIVERED;
        OrderStatus os2 = OrderStatus.valueOf("DELIVERED");

        System.out.println(os1);
        System.out.println(os2);
    }
}

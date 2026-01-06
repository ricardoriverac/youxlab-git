package application.entities;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Pedido2 {
    private static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
    private List<ItensPedido> itens = new ArrayList<>();

    private Date momento;
    private OrderStatus status;
    private Cliente cliente;

    public Pedido2(Date momento, OrderStatus status, Cliente cliente) {
        this.momento = momento;
        this.status = status;
        this.cliente = cliente;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public static SimpleDateFormat getSdf() {
        return sdf;
    }

    public static void setSdf(SimpleDateFormat sdf) {
        Pedido2.sdf = sdf;
    }

    public Date getMomento() {
        return momento;
    }

    public void setMomento(Date momento) {
        this.momento = momento;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public void setStatus(OrderStatus status) {
        this.status = status;
    }

    public List<ItensPedido> getItens() {
        return itens;
    }

    public void addItens(ItensPedido item){
        itens.add(item);
    }
    public void removeItens(ItensPedido item){
        itens.remove(item);
    }


    public Double total() {
        Double soma = 0.0;
        for (ItensPedido i : itens) {
            soma += i.subTotal();
        }
        return soma;
    }


    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Order summary: \n");
        sb.append("Momento do pedido: " + sdf.format(momento) + "\n");
        sb.append("Status do pedido: " + status + "\n");
            sb.append("Cliente: " + cliente + "\n");
            sb.append("Itens do pedido: \n");
            for(ItensPedido i : itens) {
                sb.append(i + "\n");
            }
            sb.append("Preço total: $" + total());
            return sb.toString();
        }
    }
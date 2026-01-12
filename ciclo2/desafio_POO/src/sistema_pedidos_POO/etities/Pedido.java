package sistema_pedidos_POO.etities;

import java.util.List;

public class Pedido {

    private int id;
    private Cliente cliente;
    private List<Produto> produto;
    private Endereco enderecoEntrega;
    private StatusPedido status;

    public Pedido(int id, Cliente cliente, Endereco enderecoEntrega, StatusPedido status, List<Produto> produto) {
        this.id = id;
        this.cliente = cliente;
        this.enderecoEntrega = enderecoEntrega;
        this.status = status;
        this.produto = produto;
    }

    public int getId() {
        return id;
    }

    public StatusPedido getStatus() {
        return status;
    }

    public double valorTotal() {
        double total = 0;
        for (Produto p : produto) {
            total += p.getPreco();
        }
        return total;
    }

    @Override
    public String toString() {
        return """
               Pedido id: %d
               Cliente: %s
               Endereço: %s
               Status: %s
               Produtos: %s
               Valor Total: R$ %.2f
               """.formatted(id, cliente.getNome(), enderecoEntrega, status, produto, valorTotal());
    }



}

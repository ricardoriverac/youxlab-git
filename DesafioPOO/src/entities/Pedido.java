package entities;

import java.util.List;

public class Pedido {

    Produto produto = new Produto();
    private int id;
    private Cliente cliente;
    private Endereco enderecoEntrega;
    private StatusPedido status;
    private int qntProdutos;

    public Pedido(){
    }

    public Pedido(int id, Cliente cliente, int quantidadeProdutos,Endereco enderecoEntrega, StatusPedido status) {
        this.id = id;
        this.cliente = cliente;
        this.qntProdutos = quantidadeProdutos;
        this.enderecoEntrega = enderecoEntrega;
        this.status = status;
    }


    public String toString() {
        return "\nCliente: \n"
                + cliente
                + "\nEndereço de entrega: "
                + enderecoEntrega
                + "\nProdutos: "
                + qntProdutos
                + "\nStatus inicial: "
                + status;
    }

    public int getQntProdutos() {
        return qntProdutos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Endereco getEnderecoEntrega() {
        return enderecoEntrega;
    }

    public void setEnderecoEntrega(Endereco enderecoEntrega) {
        this.enderecoEntrega = enderecoEntrega;
    }

    public StatusPedido getStatus() {
        return status;
    }

    public void setStatus(StatusPedido status) {
        this.status = status;
    }

    public void setQntProdutos(int qntProdutos) {
        this.qntProdutos = qntProdutos;
    }

    public Produto getProduto() {
        return produto;
    }

    public void setProduto(Produto produto) {
        this.produto = produto;
    }

}

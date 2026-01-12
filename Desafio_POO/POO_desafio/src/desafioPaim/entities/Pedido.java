
package desafioPaim.entities;

import desafioPaim.entities.entitiesEnums.StatusPedido;

public class Pedido {

    private int id;
    private Cliente cliente;
    private Produto produto;
    private Endereco endereco;
    private StatusPedido status;


    public Pedido(int id, Cliente cliente, Produto produto, Endereco endereco, StatusPedido status) {
        this.id = id;
        this.cliente = cliente;
        this.produto = produto;
        this.endereco = endereco;
        this.status = status;
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

    public Produto getProduto() {
        return produto;
    }

    public void setProduto(Produto produto) {
        this.produto = produto;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public StatusPedido getStatus() {
        return status;
    }

    public void setStatus(StatusPedido status) {

        this.status = status;
    }


    @Override
    public String toString() {
        return "Pedido [id=" + id +
                ", cliente=" + cliente.getName() +
                ", produto=" + produto.getName() +
                ", endereco=" + endereco +
                ", status=" + status + "]";
    }
}
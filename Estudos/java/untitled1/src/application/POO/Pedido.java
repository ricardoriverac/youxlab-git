package application.POO;

import java.util.List;

public class Pedido {
    private Integer id;
    private Cliente cliente;
    private List <Produto> list;
    private Endereco enderecoEntrega;
    private Status status;

    public Pedido(Integer id, Cliente cliente, List<Produto> list, Endereco enderecoEntrega, Status status) {
        this.id = id;
        this.cliente = cliente;
        this.list = list;
        this.enderecoEntrega = enderecoEntrega;
        this.status = status;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public List<Produto> getList() {
        return list;
    }

    public void setList(List<Produto> list) {
        this.list = list;
    }

    public Endereco getEnderecoEntrega() {
        return enderecoEntrega;
    }

    public void setEnderecoEntrega(Endereco enderecoEntrega) {
        this.enderecoEntrega = enderecoEntrega;
    }

    public Status getStatus() {
        return status;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Pedido: id=" + id + ", " + cliente + ", produtos=" + list + ", " + enderecoEntrega + ", status=" + status;
    }

}


package secao_12.entities;

import secao_12.entitiesenums.OrderStatus;

import java.util.Date;

public class Order {
    private Integer id;
    private Date monment;
    private OrderStatus status;

    public Order(){

    }

    public Order(Integer id, Date monment, OrderStatus status) {
        this.id = id;
        this.monment = monment;
        this.status = status;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public void setStatus(OrderStatus status) {
        this.status = status;
    }

    public Date getMonment() {
        return monment;
    }

    public void setMonment(Date monment) {
        this.monment = monment;
    }


    public String toString() {
        return "Order{" +
                "id=" + id +
                ", monment=" + monment +
                ", status=" + status +
                '}';
    }
}

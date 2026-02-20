package Secao9.Aula88.entities;

import java.util.Date;

public class order {
    private Date date;
    private Product product;

    public order(Date date, Product product) {
        super();
        this.date = date;
        this.product = product;
        this.product.name = "TV";
    }
    public Date getDate() {
        return date;
    }
    public void setDate(Date date) {
       this.date = date;
    }
    public Product getProduct() {
        return product;
    }
    public void setProduct(Product product) {
        this.product = product;
    }
}

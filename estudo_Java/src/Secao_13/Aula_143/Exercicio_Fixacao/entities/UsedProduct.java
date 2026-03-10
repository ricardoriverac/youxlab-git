package Secao_13.Aula_143.Exercicio_Fixacao.entities;

import java.text.SimpleDateFormat;
import java.util.Date;

public class UsedProduct extends Product{
    SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

    private Date manufactureDate;

    public UsedProduct(Date manufactureDate) {
        super();
    }

    public UsedProduct(String name, Double price, Date manufactureDate) {
        super(name, price);
        this.manufactureDate = manufactureDate;
    }

    @Override
    public String priceTag() {
        return super.name +
                " (used) " +
                "$ " +
                super.price +
                " (Manufacture date: " +
                sdf.format(manufactureDate) +
                ")";
    }
}

package secao_13.exercicioA142.entities142;

import java.time.LocalDate;
import java.util.Date;

public class UsedProduct extends Product{
    private LocalDate manufacture;

    public LocalDate getManufacture() {
        return manufacture;
    }

    public UsedProduct(String name, Double price, LocalDate manufacture) {
        super(name, price);
        this.manufacture = manufacture;
    }

    public void setManufacture(LocalDate manufacture) {
        this.manufacture = manufacture;
    }
    @Override
    public String priceTag(){
        return "Name: " + getName()
                + "\nPrice: " + getPrice()
                + "\nManufacture date (DD/MM/YYYY): " + manufacture;
    }
}

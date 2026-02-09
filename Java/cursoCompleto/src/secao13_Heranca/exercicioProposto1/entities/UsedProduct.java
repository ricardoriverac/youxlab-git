package secao13_Heranca.exercicioProposto1.entities;

import java.text.SimpleDateFormat;
import java.util.Date;

public class UsedProduct extends Product{

    SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
    private Date manufactureDate;

    public UsedProduct(String name, Double price, Date manufactureDate){
        super(name, price);
        this.manufactureDate = manufactureDate;
    }

    public Date getManufactureDate(){
        return manufactureDate;
    }
    public void setManufactureDate(){
        this.manufactureDate = manufactureDate;
    }
    @Override
    public String priceTag(){
        return "(used) $\n" +
                super.getName() + " $ " +
                super.getPrice() + "\n"+ "(Manufactured Date: $)" +
                manufactureDate;
    }



}

package secao13_Heranca.exercicioProposto1.entities;

public class ImportProduct extends Product {

    private Double customFee;

    public ImportProduct(String name, Double price, Double customFee){
        super(name, price);
        this.customFee = customFee;
    }
    public Double getCustomFee(){
        return customFee;
    }
    public void setCustomFee(Double customFee){
        this.customFee = customFee;
    }


    public Double totalPrice(){
        return super.getPrice() + customFee;
    }
    @Override
    public String priceTag(){
        return " (imported) $" +
                 super.getName() +
                "\nPrice: $" + super.priceTag() +
                "\nCustom Fee: $" + customFee +
                "\nTotal price: $" + totalPrice();
    }
}

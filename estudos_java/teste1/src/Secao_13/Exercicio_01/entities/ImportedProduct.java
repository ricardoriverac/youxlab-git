package Secao_13.Exercicio_01.entities;

public class ImportedProduct extends Product{
    private Double customsFee;

    public ImportedProduct() {
    }

    public ImportedProduct(String name, Double price, Double customsFee) {
        super(name, price);
        this.customsFee = customsFee;
    }

    public Double getCustomsFee() {
        return customsFee;
    }

    public void setCustomsFee(Double customsFee) {
        this.customsFee = customsFee;
    }

    public void totalPrice() {
        double total = super.getPrice() + this.customsFee;
    }

    @Override
    public String priceTag() {
        return String.format("%s $ %.2f (Custom fee: $ %.2f)%n",super.getName(),super.getPrice(),this.customsFee);
    }
}

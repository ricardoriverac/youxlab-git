package application.entities;

public class Converter {
    public static final double iof = 0.08;

    public static double CurrencyConverter(double quantidade, double cota){
    return quantidade * cota *(iof + 1);
    };
}

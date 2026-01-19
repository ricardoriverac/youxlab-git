package Secao_8.ExercicioParaFIxar.Calculator;

public class CurrencyCalculator {

    public static double IOF = 1.06;
    public static double convertRealToDollar (double dollar, double dollarPrice) {
        return dollar*dollarPrice*IOF;
    }
}

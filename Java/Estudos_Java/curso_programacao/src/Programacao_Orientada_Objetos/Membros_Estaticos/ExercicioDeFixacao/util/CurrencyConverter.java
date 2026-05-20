package Programacao_Orientada_Objetos.Membros_Estaticos.ExercicioDeFixacao.util;

public class CurrencyConverter {
    public static final double IOF = 0.06;

    public static double boughtReais(double dollar, double boughtDollars) {
        return (dollar * boughtDollars) + (dollar * boughtDollars * IOF);
    }
}

package secao7_introOrientacaoaObjetos.exercicioMetodosEstaticos.metodo;

public class met {
    public static double IOF = 0.06;
    public static double calcularDol(double amount, double dollarPrice) {
        return amount * dollarPrice * (1.0 + IOF);
    }
}

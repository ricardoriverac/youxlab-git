package curso_completo_java.sessao_08.pratica.exericicio04_pratica.etities;


public class CurrencyConverter {
        public static final double IOF = 0.06;

        public static double amountPaid(double dollarPrice, double amount) {
            double total = amount * dollarPrice;
            return total += total * IOF;
        }
    }


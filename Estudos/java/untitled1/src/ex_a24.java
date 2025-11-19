import java.util.Locale;

public class ex_a24 {
    public static void main(String[] args) {
        String produto1 = "Computer";
        String produto2 = "Oficce Desk";
        int idade = 30;
        int codigo = 5090;
        char genero = 'F';
        double preco1 = 2100.0;
        double preco2 = 650.50;
        double medida = 53.234567;
        System.out.printf("Products:%n %s, which price is %.2f %n %s, which price is %.2f %n %n", produto1, preco1, produto2, preco2);
        System.out.printf("Record: %d years old, code %d and gender: %s", idade, codigo, genero);
        System.out.printf("Measue with height decimal places: %f %n rouded(three decimal places): %.3f %n", medida, medida);
        Locale.setDefault(Locale.US);
        System.out.printf("US LOCALE: %.3f ", medida);
    }
}

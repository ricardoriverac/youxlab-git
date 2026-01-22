import java.util.Locale;

public class aula31 {
    public static void main(String[] args) {

        int y = 32;
        System.out.println(y);
        Locale.setDefault(Locale.US);
        double x = 10.35784;
        System.out.printf("%.2f\n", x);
        System.out.println("RESULTADO = " + x + " METROS");
        System.out.printf("RESULTADO = %.2f metros\n" , x);
        String nome = "Maria";
        int idade = 31;
        double renda = 4000.0;
        System.out.printf("%s tem %d anos e ganha R$%.2f reais \n", nome, idade, renda);
        System.out.println("Bom dia!");
    }
}

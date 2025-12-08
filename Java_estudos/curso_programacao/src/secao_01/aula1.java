package secao_01;

import java.util.Locale;

public class aula1 {
    static void main() {
        String nome = "Maria";
        int idade = 31;
        double renda = 4000.0;
        System.out.println("Olá mundo!");
        System.out.println("Bom dia!");
        double x = 10.35784;
        System.out.printf("%.2f%n", x);
        System.out.printf("%.4f%n", x );
        Locale.setDefault(Locale.US);
        System.out.printf("%.4f%n", x );
        System.out.printf("%s tem %d anos e ganha R$ %.2f reais%n", nome,idade,renda);

    }
}
package exercicios_elif;
import java.util.Locale;
import java.util.Scanner;

public class exercicio8 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        double renda = sc.nextDouble();
        double impostoRenda = 0;

        if (renda <= 2000) {
            System.out.println("ISENTO DE IMPOSTOS");

        }
        else if (renda <= 3000) {
            impostoRenda = (renda - 2000.0) * 0.08;

            System.out.printf("IMPOSTO: %.2f%n", impostoRenda);
        }
        else if (renda <= 4500) {
            impostoRenda = (renda - 3000) * 0.18 + 1000 * 0.08;
            System.out.printf("IMPOSTO: %.2f%n", impostoRenda);
        }
        else if (renda > 4500) {
            impostoRenda = (renda - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08;
            System.out.printf("IMPOSTO: %.2f%n", impostoRenda);
        }
    }
}

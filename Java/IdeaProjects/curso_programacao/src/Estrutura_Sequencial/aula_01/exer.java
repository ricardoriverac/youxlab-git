package Estrutura_Sequencial.aula_01;

import java.util.Locale;

public class exer {
    static void main() {
        String product1 = "Computer";
        String product2 = "Office desk";
        int age = 30;
        int code = 5290;
        char gender = 'F';
        double price1 = 2100.0;
        double price2 = 650.50;
        double measure = 53.234567;
        System.out.printf("%s, que o preço é $ %.2f%n", product1, price1);
        System.out.printf("%s, que o preço é $ %.2f%n", product2, price2);
        System.out.printf("Registro: %d anos, código %d e gênero %s%n", age, code, gender);
        System.out.printf("Medir tem 6 lugares decimais: %.8f%n", measure);
        System.out.printf("Simplificando (três casas decimais): %.3f%n", measure);
        Locale.setDefault(Locale.US);
        System.out.printf("US separação de deciamal %.3f", measure);
    }
}

package curso_completo_java.sessao_04.exercicios;
// Aula 25 - exercicio


import java.util.Locale;

public class exercicio01 {
    public static void main(String[] args) {

        String product1 = "Computer";
        String product2 = "Office desk";
        int age = 30;
        int code = 5290;
        char gender = 'F';
        double price1 = 2100.0;
        System.out.println(price1);
        double price2 = 650.50;
        System.out.println(price2);
        double measure = 53.234567;
        System.out.println(measure);
        System.out.printf("%s, which price is R$ %.2f %n", product1, price1);
        System.out.printf("%s, which price is R$ %.2f %n", product2, price2);
        System.out.printf("Record: %d years old, code %d and gender: %s", age, code, gender);
        System.out.printf("Measue whith eight decimal places: %f\n", measure);
        Locale.setDefault(Locale.of("pt", "BR"));          // define pt-BR como padrão
        System.out.printf("Rouded (three decimal places): %.3f \n", measure);
        Locale.setDefault(Locale.US);
        System.out.printf("US decimal points: %.3f ", measure);



    }
}

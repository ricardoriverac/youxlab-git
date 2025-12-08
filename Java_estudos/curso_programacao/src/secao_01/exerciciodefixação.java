package secao_01;

import java.util.Locale;

public class exerciciodefixação {
    static void main () {
        String product1 = "Computer";
        String product2 = "Office desk";
        int age = 30;
        int code = 5290;
        char gender = 'F';

        double prince1 = 2100.0;
        double prince2 = 650.50;
        double measure = 53.234567;
        System.out.printf("%s, which price is $ %.2f%n", product1,prince1);
        System.out.printf("Record %d years old, code %d and gender: %s%n",age, code, gender);
        System.out.printf("Measure with eight decimal places : %f%n", measure);
        System.out.printf("three decimal places: %.3f%n", measure);
        Locale.setDefault(Locale.US);
        System.out.printf("US decimal point : %.3f%n", measure );






    }
}

package Secao4.aula37;

import java.util.Locale;
import java.util.Scanner;

public class exercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
         System.out.println("Digite o valor do raio: ");
         double raio = sc.nextDouble();
         double area = Math.PI * Math.pow(raio, 2);
         System.out.println("O raio digitado foi: " + raio);
         System.out.printf("A área do círculo foi: %.4f\n", area);

         sc.close();
    }
}

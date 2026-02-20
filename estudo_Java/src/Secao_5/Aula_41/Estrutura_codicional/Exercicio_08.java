package Aula_41.Estrutura_codicional;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_08 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o valor do seu salário: ");
        double valor = sc.nextDouble();

        if (valor < 2000.01){
            System.out.println("Isento");
        }
        else if (valor < 3000.01 && valor > 2000.00) {
            valor = valor * 1.08;
            System.out.printf("o salário com o imposto %.2f", valor);
        }
        else if (valor < 4500.01 ) {
            valor = valor * 1.18;
            System.out.printf("o salário com o imposto %.2f", valor);
        }
        else if (valor > 4500.01) {
            valor = valor * 1.28;
            System.out.printf("o salário com o imposto %.2f", valor);


            // não finalizado
        }
    }
}
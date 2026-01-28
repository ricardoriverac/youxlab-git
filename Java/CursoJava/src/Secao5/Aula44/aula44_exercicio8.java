package Secao5.Aula44;

import java.util.Locale;
import java.util.Scanner;

public class aula44_exercicio8 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double imposto = 0.0;

        double valor;
        System.out.print("Digite o valor do seu salário: ");
        valor = sc.nextDouble();
        if (valor <= 2000.0) {
            System.out.print("Isento");
        } else if (valor <= 3000.0) {
            imposto = (valor - 2000.00) * 0.08;}
           else if (valor <= 4500.00) {
            imposto = (valor - 3000.00) * 0.18 + (1000.00 * 0.08);
        } else {
            imposto = (valor- 4500.00) * 0.28 + (1500.00 * 0.18) + (1000.00 * 0.08);
        }
        System.out.printf("Valor do imposto: R$%.2f", imposto);
        sc.close();
        }
    }

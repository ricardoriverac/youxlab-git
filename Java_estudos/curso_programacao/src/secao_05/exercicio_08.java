package secao_05;

import java.util.Scanner;

public class exercicio_08 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite seu salario");

        double salario = sc.nextDouble();
        double imposto = 0;

        if (salario <= 2000.0) {
            System.out.println("Isento");
        } else {

            if (salario > 2000.0 && salario <= 3000.0) {
                imposto += (salario - 2000.0) * 0.08;
            }

            if (salario > 3000.0 && salario <= 4500.0) {
                imposto += 1000.0 * 0.08;
                imposto += (salario - 3000.0) * 0.18;
            }

            if (salario > 4500.0) {
                imposto += 1000.0 * 0.08;
                imposto += 1500.0 * 0.18;
                imposto += (salario - 4500.0) * 0.28;
            }

            System.out.printf("R$ %.2f%n", imposto);
        }

        sc.close();
    }
}

package Estrutura_Sequencial.aula_03;

import java.util.Locale;
import java.util.Scanner;

public class exer4 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int fun, hora;
        double valor, sal;

        fun = sc.nextInt();
        hora = sc.nextInt();
        valor = sc.nextDouble();

        sal = (hora * valor);
        System.out.println("Funcionário = " + fun);
        System.out.printf("Salário = U$ %.2f%n ", sal);

    }
}

package curso_completo_java.sessao_04.exercicios;

/* Faça um programa para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro
casas decimais conforme exemplos.
Fórmula da área: area = π . raio^2
Considere o valor de π = 3.14159
*/

import java.util.Locale;
import java.util.Scanner;

public class exercicio_iniciante02 {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);

        double R, Area, π = 3.14159;

        R = sc.nextDouble();

        Area = π * R * R;

        System.out.printf("A=%.4f%n", Area);

        sc.close();
    }
}


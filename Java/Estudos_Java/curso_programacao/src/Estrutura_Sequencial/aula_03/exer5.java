package Estrutura_Sequencial.aula_03;

import java.util.Locale;
import java.util.Scanner;

public class exer5 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int peca1, np1, peca2, np2;
        double  v_uni1, v_uni2, pagar1, pagar2, total;

        peca1 = sc.nextInt();
        np1 = sc.nextInt();
        v_uni1 = sc.nextDouble();
        peca2 = sc.nextInt();
        np2 = sc.nextInt();
        v_uni2 = sc.nextDouble();

        pagar1 = (np1 * v_uni1);
        pagar2 = (np2 * v_uni2);
        total = (pagar1 + pagar2);
        System.out.printf("VALOR A PAGAR = R$ %.2f%n ", total);

    }
}

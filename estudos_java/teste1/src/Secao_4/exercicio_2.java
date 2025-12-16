package Secao_4;

import java.util.Scanner;
import java.util.Locale;

public class exercicio_2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite o raio de algum círculo e eu te direi a sua área");
        double a = sc.nextDouble();
        double A = Math.pow(a,2);
        double area = A * Math.PI;

        System.out.printf("O área de seu círculo é de %.4f",area);
    }
}

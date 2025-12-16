package Secao_6;

import java.util.Locale;
import java.util.Scanner;

public class exercicio_1 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        String condition;
        condition = ( number > 6) ? "não é criança" : "é criança";
        System.out.printf("Você %s",condition);
    }
}
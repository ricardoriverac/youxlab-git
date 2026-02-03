package Secao6.Aula61;

import java.util.Locale;
import java.util.Scanner;

public class aula61_exercicio4 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        double divisao = 0;
        double y, x;

        for (int i = 0; i < n; i++) {
            y = sc.nextDouble();
            x = sc.nextDouble();
            if (x == 0){
                System.out.print("Divisao impossivel");
            }else {
                divisao = y / x;
                System.out.print(divisao);
            }
        }

       sc.close();
    }
}

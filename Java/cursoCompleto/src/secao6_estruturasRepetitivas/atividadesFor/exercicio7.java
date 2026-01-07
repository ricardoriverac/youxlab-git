package secao6_estruturasRepetitivas.atividadesFor;

import java.math.MathContext;
import java.util.Scanner;
import java.lang.Math;

public class exercicio7 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int quad = 1;
        int cubo = 1;
        for (int i = 1; i <= n; i++){
            quad = (int) Math.pow(i, 2);
            cubo = (int) Math.pow(i, 3);
            System.out.println(i + " " + quad + " " + cubo);
        }
    }
}

package secao6_estruturasRepetitivas.atividadesFor;

import java.util.Scanner;

public class exercicio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 0;
        int b = 0;
        double divisao = 0;
        for (int i=0; i < n; i++) {
           a = sc.nextInt();
           b = sc.nextInt();

           if (b != 0) {
               divisao = a/b;
               System.out.println(divisao);
           }
           else {
               System.out.println("<DIVISÃO IMPOSSÍVEL>");
           }
           }
    }
}

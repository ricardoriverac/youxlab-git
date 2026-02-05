package Secao6.Aula61;

import java.util.Scanner;

public class aula61_exercicio7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        for (int i = 0; i < n; i++){
            int q = i * i;
            int c = i * i * i;
            System.out.println(i + " " + q + " " + c);
        }
        sc.close();
    }
}

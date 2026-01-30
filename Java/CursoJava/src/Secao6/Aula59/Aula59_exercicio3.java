package Secao6.Aula59;

import java.util.Scanner;

public class Aula59_exercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int y = 10;
        for (int i =0; i<4; i++){
            System.out.print(i);
            y += i;
            System.out.println(y);
        }
        sc.close();
    }
}

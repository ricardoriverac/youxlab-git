package Secao_6;

import java.util.Scanner;

public class exercicio_6 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        double number = sc.nextDouble();
        if (number<0 || 100<number) {
            System.out.println("Out of interval");
        }
        else if (number<=25) {
            System.out.println("Interval [0,25]");
        }
        else if (number<=50) {
            System.out.println("Interval [25,50]");
        }

        else if (number<=75) {
            System.out.println("Interval [50,75]");
        }
        else {
            System.out.println("Interval [75,100]");
        }
    }
}
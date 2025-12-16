package Secao_6;

import java.util.Scanner;

public class exercicio_1 {
    public static void main(String[] args) {
        int number;
        Scanner sc = new Scanner(System.in);
        System.out.println("Choose any integer number:");
        number = sc.nextInt();

        if (number<0) {
            System.out.printf("The number %d is negative!",number);
        }
        else {
            System.out.printf("The number %d is not negative",number);
        }
    }
}

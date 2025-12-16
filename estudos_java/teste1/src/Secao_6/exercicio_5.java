package Secao_6;

import java.util.Scanner;

public class exercicio_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int id, amount;
        double price, total;
        System.out.printf("-------MENU-------%n1- Hot Dog R$ 5.00%n2- X-Salad R$ 4.50%n3- X-Bacon R$ 5.00%n4- Toast   R$ 2.00%n5- Soda    R$ 2.00%nSelect your order:");
        id = sc.nextInt();
        total = 0;
        if (id==1) {
            price = 4.00;
            System.out.print("Choose the amount:");
            amount = sc.nextInt();
            total = price * amount;
            System.out.printf("The total is R$ %.2f",total);
        }
        if (id==2) {
            price = 4.50;
            System.out.print("Choose the amount:");
            amount = sc.nextInt();
            total = price * amount;
            System.out.printf("The total is R$ %.2f",total);
        }
        if (id==3) {
            price = 5.00;
            System.out.print("Choose the amount:");
            amount = sc.nextInt();
            total = price * amount;
            System.out.printf("The total is R$ %.2f",total);
        }
        if (id==4) {
            price = 2.00;
            System.out.print("Choose the amount:");
            amount = sc.nextInt();
            total = price * amount;
            System.out.printf("The total is R$ %.2f",total);
        }
        if (id==5) {
            price = 1.50;
            System.out.print("Choose the amount:");
            amount = sc.nextInt();
            total = price * amount;
            System.out.printf("The total is R$ %.2f",total);
        }
    }
}

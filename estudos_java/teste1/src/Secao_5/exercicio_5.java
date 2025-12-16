package Secao_5;

import java.util.Scanner;
import java.util.Locale;

public class exercicio_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        int firstPieceCode, secondPieceCode, firstPieceAmount, secondPieceAmount;
        double firstPiecePrice, secondPiecePrice;

        firstPieceCode = sc.nextInt();
        firstPieceAmount = sc.nextInt();
        firstPiecePrice = sc.nextDouble();
        secondPieceCode = sc.nextInt();
        secondPieceAmount = sc.nextInt();
        secondPiecePrice = sc.nextDouble();

        double totalPrice = firstPiecePrice * firstPieceAmount + secondPiecePrice * secondPieceAmount;

        System.out.printf("%nFirst Piece code:  %d%n",firstPieceCode);
        System.out.printf("Second Piece code: %d%n",secondPieceCode);
        System.out.printf("Amount to pay: R$ %.2f", totalPrice);
    }
}

package application;

import application.entities.Converter;

import java.sql.SQLOutput;
import java.util.Locale;
import java.util.Scanner;

public class a_78_ex {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, qual o preço do dolár? ");
        double dolarPreco = sc.nextDouble();
        System.out.print("Caro usuário, quantos doláres você deseja comprar?");
        double dolarQuantidade = sc.nextDouble();
        System.out.print("Caro usuário, você terá que pagar " + Converter.CurrencyConverter(dolarQuantidade, dolarPreco));
    }
}

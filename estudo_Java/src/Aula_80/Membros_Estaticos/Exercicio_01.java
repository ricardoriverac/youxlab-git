package Aula_80.Membros_Estaticos;

import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.NotNull;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_01 {

    public static double CurrencyConverter(double valorDolar, double quantidadeDolar) {
        double totalApagar = (quantidadeDolar * 1.06) * valorDolar;
        return totalApagar;
    }

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o preço em dólar: ");
        double valor1 = sc.nextDouble();

        System.out.print("Digite a quantidade de dolar será comprados: ");
        double valor2 = sc.nextDouble();

        System.out.print(CurrencyConverter(valor1, valor2));
    }

}

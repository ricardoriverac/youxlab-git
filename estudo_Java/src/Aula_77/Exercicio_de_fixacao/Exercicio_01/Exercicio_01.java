package Aula_77.Exercicio_de_fixacao.Exercicio_01;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_01 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Calculo_Retangulo retangulo = new Calculo_Retangulo();

        System.out.print("Digite a largura do retângulo: ");
        retangulo.largura = sc.nextDouble();

        System.out.print("Digite a altura do retângulo: ");
        retangulo.altura = sc.nextDouble();

        System.out.printf("AREA = %.2f %n", retangulo.area());
        System.out.printf("PERIMETRO = %.2f %n", retangulo.perimetro());
        System.out.printf("DIAGONAL = %.2f", retangulo.diagonal());

    }
}
package Estrutura_sequencial04.exercicios;

/*
        Fazer um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por
hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas
decimais.
 */

import java.util.Scanner;

public class exercicio_iniciante04 {

    public static void main(String[] ags) {

        Scanner sc = new Scanner(System.in);

        double horas_trabalhadas, salario_hora, salario;

        horas_trabalhadas = sc.nextDouble();
        salario_hora = sc.nextDouble();

        salario = salario_hora / horas_trabalhadas;

        System.out.printf("Seu salário por hora é = %.2f%n", salario);
    }
}

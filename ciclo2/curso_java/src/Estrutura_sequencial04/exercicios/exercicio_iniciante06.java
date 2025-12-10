package Estrutura_sequencial04.exercicios;

/* Fazer um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e
mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
*/

import java.util.Scanner;

public class exercicio_iniciante06 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double A, B, C;
        double triangulo , circulo, trapezio, quadrado, retangulo;
        double elevado;

        System.out.println("→ números com virgula e duas casas decimais ←");
        System.out.println("Digite o primeiro valor:");
        A = sc.nextDouble();
        System.out.println("Digite o segundo valor:");
        B = sc.nextDouble();
        System.out.println("Digite o terceiro valor:");
        C = sc.nextDouble();

        elevado = Math.pow(C, 2);

        triangulo = ( A * C ) / 2;

        circulo = 3.14159 * elevado ;

        trapezio = (( A + B) * C ) / 2;

        quadrado = B * B;

        retangulo = A * B;

        System.out.printf(" A área do triangulo retangulo é: %.2f\n", triangulo);
        System.out.printf("A área de circulo é: %.2f\n", triangulo);
        System.out.printf("A área do trapézio é: %.2f\n", trapezio);
        System.out.printf("A area do quadrado é de: %.2f\n", quadrado);
        System.out.printf("A área do retangulo é: %.2f\n", retangulo);







    }
    }


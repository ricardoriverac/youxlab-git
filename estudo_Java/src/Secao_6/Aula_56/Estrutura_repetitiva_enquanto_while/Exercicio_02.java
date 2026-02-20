package Aula_56.Estrutura_repetitiva_enquanto_while;

import java.util.Scanner;

public class Exercicio_02 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double Coordenada_X, Coordenada_Y;

        System.out.print("Digite a coordenada X: ");
        Coordenada_X = sc.nextDouble();

        System.out.print("Digite a coordenada Y: ");
        Coordenada_Y = sc.nextDouble();

        while (Coordenada_X != 0 && Coordenada_Y != 0){

            if (Coordenada_X > 0 && Coordenada_Y > 0){
                System.out.println("1º Quadrante");
            }
            else if (Coordenada_X < 0 && Coordenada_Y > 0) {
                System.out.println("2º Quadrante");
            }
            else if (Coordenada_X < 0 && Coordenada_Y < 0) {
                System.out.println("3º Quadrante");
            }
            else if (Coordenada_X > 0 && Coordenada_Y < 0) {
                System.out.println("4º Quadrante");
            }
            System.out.print("Digite a coordenada X novamente: ");
            Coordenada_X = sc.nextDouble();

            System.out.print("Digite a coordenada Y novamente: ");
            Coordenada_Y = sc.nextDouble();
        }
    }
}
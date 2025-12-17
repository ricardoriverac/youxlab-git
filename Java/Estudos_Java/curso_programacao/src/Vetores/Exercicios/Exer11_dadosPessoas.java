package Vetores.Exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Exer11_dadosPessoas {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantas pessoas serão digitas? ");
        int qntPessoas = sc.nextInt();
        double[] vetorAltura = new double[qntPessoas];
        char[] vetorGenero = new char[qntPessoas];

        for (int i = 0; i < qntPessoas; i++) {
            System.out.print("Altura da " + (i+1) + "a pessoa: ");
            vetorAltura[i] = sc.nextDouble();
            System.out.print("Genero da " + (i+1) + "a pessoa: ");
            vetorGenero[i] = sc.next().charAt(0);
        }

        double menorAltura = vetorAltura[0], maiorAltura = vetorAltura[0];
        for (int i = 0; i < qntPessoas; i++) {
            if (maiorAltura < vetorAltura[i]) {
                maiorAltura = vetorAltura[i];
            }
            else if (menorAltura > vetorAltura[i]) {
                menorAltura = vetorAltura[i];
            }
        }
        System.out.println("Menor altura = " + menorAltura);
        System.out.println("Maior altura = " + maiorAltura);


        double somaAlturaMulher = 0;
        double mediaAlturaMulher = 0;
        int qntHomens = 0;

        for (int i = 0; i < qntPessoas; i++) {
            if ('F' == vetorGenero[i]){
                somaAlturaMulher = vetorAltura[i];
                mediaAlturaMulher += somaAlturaMulher / vetorAltura.length;
            }
            else {
                qntHomens++;
            }
        }

        System.out.printf("Media das alturas das mulheres = %.2f%n", mediaAlturaMulher);
        System.out.println("Numero de homens = " + qntHomens);

        sc.close();
    }
}

package curso_completo_java.sessao_10.exercicios;

/*Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
de homens. */

import java.util.Locale;
import java.util.Scanner;

public class exercicio11 {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            int numeros, quantidadeHomens, quantidadeMulheres;
            double menorAltura, maiorAltura, alturaMediaF, alturaTotalF;

            System.out.print("Quantas pessoas serão digitadas?: ");
            numeros = sc.nextInt();

            double[] alturas = new double[numeros];
            char[] generos = new char[numeros];

            for (int i=0; i<numeros; i++) {
                System.out.printf("Altura da %dª pessoa: ", i + 1);
                alturas[i] = sc.nextDouble();
                System.out.printf("Genêro da %dª pessoa: ", i + 1);
                generos[i] = sc.next().charAt(0);
            }

            menorAltura = alturas[0];
            maiorAltura = alturas[0];

            for (int i=1; i<numeros; i++) {
                if (alturas[i] > maiorAltura) {
                    maiorAltura = alturas[i];
                }
                if (alturas[i] < menorAltura) {
                    menorAltura = alturas[i];
                }
            }

            quantidadeHomens = 0;
            quantidadeMulheres = 0;
            alturaTotalF = 0;
            for (int i=0; i<numeros; i++) {
                if (generos[i]=='M') {
                    quantidadeHomens++;
                }
                else {
                    quantidadeMulheres++;
                    alturaTotalF = alturaTotalF + alturas[i];
                }
            }

            alturaMediaF = alturaTotalF / quantidadeMulheres;

            System.out.printf("Menor altura: %.2f\n", menorAltura);
            System.out.printf("Maior altura: %.2f\n", maiorAltura);
            System.out.printf("Média das alturas das mulheres: %.2f\n", alturaMediaF);
            System.out.printf("Numero de homens: %d\n", quantidadeHomens);

            sc.close();
        }
    }


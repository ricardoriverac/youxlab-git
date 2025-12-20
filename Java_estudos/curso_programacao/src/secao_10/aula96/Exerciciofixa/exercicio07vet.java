package secao_10.aula96.Exerciciofixa;

import java.util.Locale;
import java.util.Scanner;

public class exercicio07vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Quantos elementos vai ter o vetor? ");
        int numerosvetor = sc.nextInt();
        double[] vetorA = new double[numerosvetor];


        for (int i = 0; i < numerosvetor; i++) {
            System.out.println("Digite um numero: ");
            vetorA[i] = sc.nextDouble();
        }

        System.out.println("Media dos pares: ");
        double somaPares = 0;
        int countPares = 0;
        for (int i = 0; i < numerosvetor; i++) {
            if (vetorA[i] % 2 == 0) {
                somaPares += vetorA[i];
                countPares++;
            }
        }
        if (somaPares == 0 ){
            System.out.println("NENHUM NUMERO PAR");
        }else{
            System.out.println("media dos pares:" + somaPares / countPares);
        }

    }
}

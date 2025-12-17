package curso_completo_java.sessao_10.exercicios;

/* Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
da pessoa mais velha */

import java.util.Locale;
import java.util.Scanner;

public class exercicio09 {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            int numero, maiorIdade, posicaoMaior;

            System.out.print("Quantas pessoas voce vai digitar? ");
            numero = sc.nextInt();

            String[] nomes = new String[numero];
            int[] idades = new int[numero];

            for (int i=0; i<numero; i++) {
                System.out.printf("Dados da %dª pessoa:\n", i + 1);
                System.out.print("Nome: ");
                nomes[i] = sc.next();
                System.out.print("Idade: ");
                idades[i] = sc.nextInt();
            }

            maiorIdade = idades[0];
            posicaoMaior = 0;

            for (int i=1; i<numero; i++) {
                if (idades[i] > maiorIdade) {
                    maiorIdade = idades[i];
                    posicaoMaior = i;
                }
            }

            System.out.printf("Pessoa mais velha: %s\n", nomes[posicaoMaior]);

            sc.close();
        }
    }


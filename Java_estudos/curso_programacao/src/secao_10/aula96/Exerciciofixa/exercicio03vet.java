package secao_10.aula96.Exerciciofixa;

import java.util.Locale;
import java.util.Scanner;

public class exercicio03vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Quantas pessoas você quer digitar? ");
        int qntPessoas = sc.nextInt();
        String[] nomes = new String[qntPessoas];
        int[] idades = new int[qntPessoas];

        for (int i = 0; i < qntPessoas; i++) {
            System.out.println("Dados da " + (i + 1) + "a pessoa: ");
            System.out.print("Name: ");
            nomes[i] = sc.next();

            System.out.print("Age: ");
            idades[i] = sc.nextInt();

        }

        int maioridade = idades[0];
        int posicaomaior = 0;

        for (int i = 1; i < qntPessoas; i++) {
            if (idades[i] > maioridade) {
                maioridade = idades[i];
                posicaomaior = i;
            }
        }

        System.out.println("Pessoa mais velha é: " + nomes[posicaomaior]);

    }
}